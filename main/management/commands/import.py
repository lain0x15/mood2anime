from django.core.management.base import BaseCommand, CommandError
from main.models import genres, types_model, studios, franchises, anime, screenshots
import yaml, os, glob, hashlib
from pathlib import Path
from django.core.files import File
import main
import django

def get_yamls_by_path(path):
    return glob.glob(f"{path}/*.yml")

def import_franchise(name):
    franchises.objects.update_or_create(name=name)

class Command(BaseCommand):
    help = 'Import animes/franchises/genres/kind/studios'

    def __log(self, msg):
        print(msg)

    def __import_studio(self, name, imageName):
        if not imageName:
            studios.objects.update_or_create (
                name=name,
                defaults={
                    'image': None
                }
            )
        else:
            with open(Path(f'{self.base_path}/studios/picture') / imageName, 'rb') as file:
                studios.objects.update_or_create (
                    name=name,
                    defaults={
                        'image': File(file, name=imageName)
                    }
                )

    def __import_anime(self, animeField):
        with open(Path(f'{self.base_path}/animes/portraitImage') / animeField['portraitImgName'], 'rb') as file:
            createdAnime, created = anime.objects.update_or_create (
                url_name=animeField['url_name'],
                defaults={
                    'name': animeField['name'],
                    'releaseYear': animeField['releaseYear'],
                    'review': animeField['review'],
                    'description': animeField['description'],
                    'portraitImage': File(file, name=animeField['portraitImgName']),
                    'type_field': types_model.objects.get(name=animeField['typeName']),
                    'episodes': animeField.get('episodes', None),
                    'franchise': franchises.objects.get(name=animeField['franchise']) if animeField['franchise'] else None
                }
            )
        if animeField.get('studios', None):
            for anime_studio in createdAnime.studio.all():
                if not anime_studio.name in animeField['studios']:
                    createdAnime.studio.remove(anime_studio)
            existed_studios = [st.name for st in createdAnime.studio.all()]
            for animeStudioName in animeField['studios']:
                if not animeStudioName in existed_studios:
                    try:
                        createdAnime.studio.add(studios.objects.get(name=animeStudioName))
                    except main.models.studios.DoesNotExist:
                        raise Exception(f'Студии {animeStudioName}, не существует')

        if animeField.get('genres', None):
            for anime_genre in createdAnime.genres.all():
                if not anime_genre.name in animeField['genres']:
                    createdAnime.genres.remove(anime_genre)
            existed_genres = [ge.name for ge in createdAnime.genres.all()]
            for genre in animeField['genres']:
                if not genre in existed_genres:
                    createdAnime.genres.add(genres.objects.get(name=genre))


        existed_files_hash = []
        for screenshot in screenshots.objects.filter(anime_id=createdAnime):
            file_hash = hashlib.md5()
            with screenshot.screenshot.open('rb') as file:
                fb = file.read(65536)
                while len(fb) > 0:
                    file_hash.update(fb)
                    fb = file.read(65536)
            existed_files_hash.append(file_hash.hexdigest())

        screenshots_hash = []
        for screenshot in animeField.get('screenshots', []):
            file_hash = hashlib.md5()
            with open(Path(f'{self.base_path}/animes/screenshots') / screenshot, 'rb') as file:
                fb = file.read(65536)
                while len(fb) > 0:
                    file_hash.update(fb)
                    fb = file.read(65536)

                screenshots_hash.append(file_hash.hexdigest())
                if not screenshots_hash[-1] in existed_files_hash:
                    screenshots.objects.create(
                        screenshot = File(file, name=screenshot),
                        anime_id = createdAnime
                    )

        for screenshot in screenshots.objects.filter(anime_id=createdAnime):
            file_hash = hashlib.md5()
            with screenshot.screenshot.open('rb') as file:
                fb = file.read(65536)
                while len(fb) > 0:
                    file_hash.update(fb)
                    fb = file.read(65536)
            if not file_hash.hexdigest() in screenshots_hash:
                screenshot.delete()

    def add_arguments(self, parser):
        parser.add_argument('--path', nargs='+', type=str)

    def handle(self, *args, **options):
        if options['path'] is None:
            raise CommandError('Опция path не задана')

        self.base_path = f'{options["path"][0]}'

        for file_path in get_yamls_by_path(f"{self.base_path}/genres"):
            with open(file_path, 'r', encoding="utf8") as file:
                loaded_genres = yaml.safe_load(file)
            for genre in loaded_genres:
                genres.objects.update_or_create(name=genre)

        for file_path in get_yamls_by_path(f"{self.base_path}/kind"):
            with open(file_path, 'r', encoding="utf8") as file:
                loaded_kind = yaml.safe_load(file)
            for kind in loaded_kind:
                types_model.objects.update_or_create (name=kind['name'], defaults={'show_in_search': kind['show_in_search']})

        for file_path in get_yamls_by_path(f"{self.base_path}/studios"):
            with open(file_path, 'r', encoding="utf8") as file:
                loaded_studios = yaml.safe_load(file)
            for studio in loaded_studios:
                self.__import_studio(name=studio['name'], imageName=studio['imageName'])

        for file_path in get_yamls_by_path(f"{self.base_path}/franchises"):
            with open(file_path, 'r', encoding="utf8") as file:
                loaded_franchises = yaml.safe_load(file)
            for franchise in loaded_franchises:
                import_franchise(name=franchise)

        for file_path in get_yamls_by_path(f"{self.base_path}/animes"):
            with open(file_path, 'r', encoding="utf8") as file:
                loaded_animes = yaml.safe_load(file)
            for animeField in loaded_animes:
                self.__import_anime(animeField)

        self.stdout.write(
            self.style.SUCCESS('Success')
        )