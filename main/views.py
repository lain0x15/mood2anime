from django.shortcuts import render, redirect, get_object_or_404
from .models import anime, genres, genreAnime
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
    pageLimit = 25
    try:
        page = int(request.GET.get('page', 1))
        page = page if page >= 1 else 1
    except ValueError:
        page = 1

    min_date_release = anime.objects.order_by('releaseYear')[0].releaseYear.year
    max_date_release = datetime.datetime.now().year

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

    animes = anime.objects.filter(releaseYear__range=(
        date_release_from,
        date_release_to
    ))

    if animes.count() != 0:
        pages = ceil(animes.count()/pageLimit)
        page = pages if page > pages else page
        animes = animes[pageLimit * (page - 1):pageLimit * page]
    else:
        pages = 0
        page = 0

    return render(request, "listAnimePage.html", context={
    'animes':animes,
    'pages':pages,
    'currentPage':page,
    'anime_filter':
    {
        'min_date_release': min_date_release,
        'max_date_release': max_date_release,
        'date_from':date_release_from.year,
        'date_to': date_release_to.year
    }
    })

def animePage(request, url_name):
    animeContext = get_object_or_404(anime, url_name=url_name)
    return render(request, "anime.html", context={'anime': animeContext})

def getIDsAnime(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    animeIDs = anime.objects.all()

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
        'trailer': responseAnime.trailer,
        'releaseYear': responseAnime.releaseYear,
        'review': responseAnime.review,
        'description': responseAnime.description,
        'genre': [genre.genreID.name for genre in responseAnime.getGenres()]
    }
    response = JsonResponse({'status': 'ok', 'anime':animeDict})
    return response

def getAnimesByFilters(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    min_date_release = anime.objects.order_by('releaseYear')[0].releaseYear.year
    max_date_release = datetime.datetime.now().year

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

    animes = anime.objects.filter(releaseYear__range=(
        date_release_from,
        date_release_to
    ))

    pageLimit = 25
    pages = 0
    try:
        page = int(request.POST.get('page', 1))
        page = page if page >= 1 else 1
    except ValueError:
        page = 1

    if animes.count() != 0:
        pages = ceil(animes.count()/pageLimit)
        page = pages if page > pages else page
        animes = [{
            'name': anime.name,
            'portraitImage': anime.portraitImage.url,
            'releaseYear': anime.releaseYear,
            'genre': [genre.genreID.name for genre in anime.getGenres()],
            'description': anime.description,
            'url_name': anime.url_name
        } for anime in animes[pageLimit * (page - 1):pageLimit * page]]
    else:
        animes = []

    print(animes)
    response = JsonResponse({'status': 'ok', 'animes':animes, 'page': page, 'pages': pages})
    return response

def sitemap(request):
    animeList = anime.objects.all()
    return render(request, 'sitemap.xml', context={'animeList': animeList, 'website_dns_name': settings.WEBSITE_DNS_NAME}, content_type='application/xml')