from django.shortcuts import render, redirect, get_object_or_404
from .models import anime, genres, types_model
from django.http import JsonResponse, HttpResponse
import datetime
from django.conf import settings
import json
import random
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect
from math import ceil

def homePage(request):
    return render(request, "homePage.html")

def listAnimePage(request):
    min_date_release = anime.objects.filter(releaseYear__isnull=False).order_by('releaseYear').first().releaseYear.year
    max_date_release = anime.objects.filter(releaseYear__isnull=False).order_by('releaseYear').last().releaseYear.year

    try:
        date_release_from = int(request.GET.get('date_release_from', min_date_release))
        date_release_from = datetime.datetime(date_release_from, 1, 1)
    except ValueError:
        date_release_from = datetime.datetime(min_date_release, 1, 1)
    try:
        date_release_to = int(request.GET.get('date_release_to', max_date_release))
        date_release_to = datetime.datetime(date_release_to, 1, 1)
    except ValueError:
        date_release_to = datetime.datetime(max_date_release, 1, 1)

    genresFilter = genres.objects.all()

    selected_genres_req = request.GET.get('filter_genres', '').split('-')
    selected_genres = []
    selected_genres_and = []
    for selected_genre in selected_genres_req:
        try:
            if int(selected_genre.split('_')[0]) == 1:
                selected_genres.append(int(selected_genre.split('_')[1]))
            elif int(selected_genre.split('_')[0]) == 2:
                selected_genres_and.append(int(selected_genre.split('_')[1]))
        except ValueError:
            pass

    try:
        order_by = int(request.GET.get('order_by', 0))
    except ValueError:
        order_by = 0

    return render(request, "listAnimePage.html", context={
    'anime_filter':
        {
            'min_date_release': min_date_release,
            'max_date_release': max_date_release,
            'date_from':date_release_from.year,
            'date_to': date_release_to.year,
            'genres': genresFilter,
            'selected_genres': selected_genres,
            'selected_genres_and': selected_genres_and,
            'order_by': order_by
        }
    })

def animePage(request, url_name):
    animeContext = get_object_or_404(anime, url_name=url_name)
    return render(request, "anime.html", context={'anime': animeContext})

def getIDsAnime(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    animeIDs = anime.objects.all()
    animeIDs = animeIDs.filter(type_field__in=types_model.objects.filter(show_in_search=True))
    animeIDs = animeIDs.filter(description__isnull=False).exclude(description__exact='').order_by('?')[:500]

    animeIDs = [animeRow.id for animeRow in animeIDs]
    response = JsonResponse({'status': 'ok', 'animeIDs':animeIDs})
    return response

def getAnimeByID (request, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        responseAnime = anime.objects.get(id=int(id))
    except anime.DoesNotExist:
        return HttpResponseNotFound()

    animeDict = {
        'url_name': responseAnime.url_name,
        'name': responseAnime.name,
        'releaseYear': responseAnime.releaseYear,
        'review': responseAnime.review,
        'description': responseAnime.description,
        'genre': [genre.name for genre in responseAnime.genres.all()],
        'screenshots': [screenshot.screenshot.url for screenshot in responseAnime.getAnimeScreenshots()]
    }
    response = JsonResponse({'status': 'ok', 'anime':animeDict})
    return response

def get_anime(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        limit = int(request.POST.get('limit', 25))
    except ValueError:
        limit = 25
    limit = limit if 1 <= limit and limit <= 25 else 25

    try:
        page = int(request.POST.get('page', 1))
    except ValueError:
        page = 1
    page = page if page >= 1 else 1
    pages = 0

    min_date_release = anime.objects.filter(releaseYear__isnull=False).order_by('releaseYear').first().releaseYear.year
    max_date_release = anime.objects.filter(releaseYear__isnull=False).order_by('releaseYear').last().releaseYear.year
    try:
        date_release_from = int(request.POST.get('date_release_from', min_date_release))
        date_release_from = datetime.datetime(date_release_from, 1, 1)
    except ValueError:
        date_release_from = datetime.datetime(min_date_release, 1, 1)
    try:
        date_release_to = int(request.POST.get('date_release_to', max_date_release))
        date_release_to = datetime.datetime(date_release_to, 1, 1)
    except ValueError:
        date_release_to = datetime.datetime(max_date_release, 1, 1)

    selected_genres_req = request.POST.get('filter_genres', '').split('-')
    selected_genres = []
    selected_genres_and = []
    for selected_genre in selected_genres_req:
        try:
            if int(selected_genre.split('_')[0]) == 1:
                selected_genres.append(int(selected_genre.split('_')[1]))
            elif int(selected_genre.split('_')[0]) == 2:
                selected_genres_and.append(int(selected_genre.split('_')[1]))
        except ValueError:
            pass

    try:
        order_by = int(request.POST.get('order_by', 0))
    except ValueError:
        order_by = 0

    animes = anime.objects.all()

    if selected_genres:
        animes = animes.filter(genres__in=selected_genres).distinct()
    if selected_genres_and:
        for selected_genre_and in selected_genres_and:
            animes = animes.filter(genres=selected_genre_and)

    if date_release_from.year != min_date_release or date_release_to.year != max_date_release:
        animes = animes.filter(
            releaseYear__range=(
                date_release_from,
                date_release_to
            )
        )

    animes = animes.filter(type_field__in=types_model.objects.filter(show_in_search=True))

    if order_by == 1:
        animes = animes.order_by('-releaseYear', '-review')
    elif order_by == 2:
        animes = animes.order_by('releaseYear', '-review')
    elif order_by == 3:
        animes = animes.order_by('-review')
    elif order_by == 4:
        animes = animes.order_by('review')
    else:
        animes = animes.order_by('-id')

    if animes.count() != 0:
        pages = ceil(animes.count()/limit)
        page = pages if page > pages else page
        animes = [{
            'url_name': anime.url_name,
            'name': anime.name,
            'releaseYear': anime.releaseYear,
            'review': anime.review,
            'description': anime.description,
            'kind': anime.type_field.name,
            'portraitImage': anime.portraitImage.url,
            'genre': [genre.name for genre in anime.genres.all()]
        } for anime in animes[limit * (page - 1):limit * page]]
    else:
        animes = []

    response = JsonResponse({'animes':animes, 'page': page, 'pages': pages})
    return response

def sitemap(request):
    animeList = anime.objects.all()
    return render(request, 'sitemap.xml', context={'animeList': animeList, 'website_dns_name': settings.WEBSITE_DNS_NAME}, content_type='application/xml')