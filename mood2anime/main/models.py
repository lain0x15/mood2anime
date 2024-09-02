from django.db import models

# Create your models here.
class mood(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img/genresImg/')
    
    def __str__(self):
        return self.name
    
class genres(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class anime(models.Model):
    name = models.CharField(max_length=50)
    trailer = models.URLField(max_length=200)
    releaseYear = models.DateField()
    review = models.FloatField(default=0.0)
    description = models.CharField(max_length=375)
    
    def getGenres(self):
        return genreAnime.objects.filter(animeID=self)

    def __str__(self):
        return self.name

class genreAnime(models.Model):
    genreID = models.ForeignKey(genres, on_delete=models.CASCADE)
    animeID = models.ForeignKey(anime, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.genreID.name + ' | ' + self.animeID.name

class moodAnime(models.Model):
    moodID = models.ForeignKey(mood, on_delete=models.CASCADE)
    animeID = models.ForeignKey(anime, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.moodID.name + ' | ' + self.animeID.name