from django.db import models

# Create your models here.
class genres(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class studios (models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='studios/picture/')

    def __str__(self):
        return self.name

class types_model (models.Model):
    name = models.CharField(max_length=50)

class franchises (models.Model):
    name = models.CharField(max_length=50)

class anime(models.Model):
    url_name = models.CharField(max_length=50, unique=True, null=False)
    name = models.CharField(max_length=50)
    trailer = models.URLField(max_length=200)
    releaseYear = models.DateField()
    review = models.FloatField(default=0.0)
    description = models.CharField(max_length=375)
    portraitImage = models.ImageField(upload_to='anime/portraitImage/')
    studio = models.ManyToManyField(studios)
    type_field = models.ForeignKey(types_model, on_delete=models.PROTECT, null=True)
    franchise = models.ForeignKey(franchises, on_delete=models.PROTECT, null=False)

    def getGenres(self):
        return genreAnime.objects.filter(animeID=self)

    def getFranchisesAnime(self):
        return anime.objects.filter(franchise=self.franchise.id).order_by('releaseYear')

    def __str__(self):
        return self.name

class genreAnime(models.Model):
    genreID = models.ForeignKey(genres, on_delete=models.CASCADE)
    animeID = models.ForeignKey(anime, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.genreID.name + ' | ' + self.animeID.name