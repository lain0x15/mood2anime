from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(mood)
admin.site.register(genres)
admin.site.register(anime)
admin.site.register(genreAnime)
admin.site.register(moodAnime)