from django.shortcuts import render, redirect
from .models import mood, moodAnime, anime, genres, genreAnime
from django.http import JsonResponse, HttpResponse
import datetime
from django.conf import settings
import json
import random
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest

def index(request):
    moods = mood.objects.all()
    return render(request, "homePage.html", context={'moods':moods})

def moodAnimeView(request, id):
    try:
        _mood = mood.objects.get(id=id)
    except mood.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, "animePage.html", context={'mood':_mood})

def getIDsAnime(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    animeIDs = anime.objects.all()

    search_filter_genre = request.POST.get("search_filter_genre", "")
    search_filter_mood = request.POST.get("search_filter_mood", "")

    if search_filter_genre == "":
        _genres = genres.objects.all()
    else:
        search_filter_genre = search_filter_genre.split(',')
        _genres = genres.objects.filter(id__in=search_filter_genre)
        for animeRow in animeIDs:
            animeGenres = animeRow.getGenres()
            for i in _genres:
                if not animeGenres.filter(genreID=i):
                    animeIDs = animeIDs.exclude(id=animeRow.id)
                    break

    if search_filter_mood == "":
        _moods = mood.objects.all()
    else:
        search_filter_mood = search_filter_mood.split(',')
        _moods = mood.objects.filter(id__in=search_filter_mood)
        for animeRow in animeIDs:
            animeMoods = animeRow.getMoods()
            for i in _moods:
                if not animeMoods.filter(moodID=i):
                    animeIDs = animeIDs.exclude(id=animeRow.id)
                    break

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
        'name': responseAnime.name,
        'trailer': responseAnime.trailer,
        'releaseYear': responseAnime.releaseYear,
        'review': responseAnime.review,
        'description': responseAnime.description,
        'genre': [genre.genreID.name for genre in responseAnime.getGenres()]
    }
    response = JsonResponse({'status': 'ok', 'anime':animeDict})
    return response