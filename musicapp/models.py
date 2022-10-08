from django.db import models


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    

class Song(models.Model):
    title = models.CharField(max_length=200)
    released = models.DateField()
    likes = models.TextField(max_length=200)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Attributes(models.Model):
    content = models.TextField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)