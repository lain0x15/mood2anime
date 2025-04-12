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

    animes = anime.objects.all()
    pages = ceil(animes.count()/pageLimit)
    page = pages if page > pages else page
    animes = animes[pageLimit * (page - 1):pageLimit * page]
    return render(request, "listAnimePage.html", context={'animes':animes, 'pages':pages, 'currentPage':page})

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