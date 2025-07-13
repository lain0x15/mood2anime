"""mood2anime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as mainViews
from extend_auth import views as extend_auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', mainViews.homePage, name = 'home'),
    path('listAnimePage', mainViews.listAnimePage, name = 'listAnimePage'),
    path('animePage/<str:url_name>', mainViews.animePage, name = 'animePage'),
    path('getAnimeByID/<int:id>', mainViews.getAnimeByID, name="getAnimeByID"),
    path('getIDsAnime', mainViews.getIDsAnime, name="getIDsAnime"),
    path('api/anime/get', mainViews.get_anime, name="get_anime"),
    path('sitemap.xml', mainViews.sitemap, name="sitemap"),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/signup/', extend_auth_views.signup, name='signup'),
    path('accounts/profile/', extend_auth_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)