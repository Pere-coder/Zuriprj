from django.contrib import admin

from .models import Artiste, Song, Attributes

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Attributes)
