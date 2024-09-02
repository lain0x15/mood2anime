from django.shortcuts import render, redirect
from .models import mood, moodAnime, anime
from django.http import JsonResponse, HttpResponse
import datetime
from django.conf import settings
import json
import random

# Create your views here.
def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )

def index(request):
    moods = mood.objects.all()
    return render(request, "homePage.html", context={'moods':moods})

def moodAnimeView(request, id):
    if request.method == "GET":
        _mood = mood.objects.get(id=id)
        _moodAnime = moodAnime.objects.filter(moodID=_mood)
        animes = [moodAnimeOne.animeID for moodAnimeOne in _moodAnime]
        response = render(request, "animePage.html", context={'mood':_mood})
        response.delete_cookie('animesIDs')
        response.delete_cookie('animeOffset')
        return response
    elif request.method == "POST":
        if not request.COOKIES.get('animesIDs'):
            _mood = mood.objects.get(id=id)
            _moodAnime = moodAnime.objects.filter(moodID=_mood)
            animes = [moodAnimeOne.animeID.id for moodAnimeOne in _moodAnime]
            animesIDs = animes
            random.shuffle(animesIDs)
            animeOffset = 0
        else:
            animesIDs = json.loads(request.COOKIES.get('animesIDs'))
            animeOffset = int(request.COOKIES.get('animeOffset'))
            animeOffset = animeOffset - 1 if bool(request.POST.get('previous')=='1') else animeOffset + 1
            if len(animesIDs) <= animeOffset:
                animeOffset = 0
            elif animeOffset < 0:
                animeOffset = len(animesIDs) - 1
        
        try:
            responseAnime = anime.objects.get(id=animesIDs[animeOffset])
        except anime.DoesNotExist:
            return redirect ('mood', id=id)

            
        
        animeDict = {'name': responseAnime.name,
               'trailer': responseAnime.trailer,
               'releaseYear': responseAnime.releaseYear,
               'review': responseAnime.review,
               'description': responseAnime.description,
               'genre': [genre.genreID.name for genre in responseAnime.getGenres()]
               }
        response = JsonResponse({'status': 'ok', 'anime':animeDict})
        set_cookie(response, 'animesIDs', animesIDs)
        set_cookie(response, 'animeOffset', animeOffset)
        return response