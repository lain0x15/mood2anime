from django.db import models

# Create your models here.
class genres(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    
    def __str__(self):
        return self.name

class studios (models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    image = models.ImageField(upload_to='studios/picture/', null=True)

    def __str__(self):
        return self.name

class types_model (models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    show_in_search = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class franchises (models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

class anime(models.Model):
    url_name = models.CharField(max_length=50, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    releaseYear = models.DateField(null=False)
    review = models.FloatField(default=0.0, null=False)
    portraitImage = models.ImageField(upload_to='anime/portraitImage/', null=False)
    type_field = models.ForeignKey(types_model, on_delete=models.PROTECT, null=False)

    franchise = models.ForeignKey(franchises, on_delete=models.PROTECT, null=True)
    description = models.CharField(max_length=500, null=True)
    studio = models.ManyToManyField(studios)
    episodes = models.IntegerField(null=True)
    genres = models.ManyToManyField(genres)

    def getFranchisesAnime(self):
        if not self.franchise:
            return anime.objects.filter(id=self.id)
        return anime.objects.filter(franchise=self.franchise.id).order_by('releaseYear')

    def getAnimeScreenshots(self):
        return screenshots.objects.filter(anime_id = self.id)

    def __str__(self):
        return self.name

class screenshots(models.Model):
    screenshot = models.ImageField(upload_to='anime/screenshots/', null=False)
    anime_id = models.ForeignKey(anime, on_delete=models.CASCADE, null=False)