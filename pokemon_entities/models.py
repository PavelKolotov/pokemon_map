from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return '{}'.format(self.title)
# your models here1
class PokemonEntity(models.Model):
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)

    def __str__(self):
        return '{} or {}'.format(self.lat, self.lon)
