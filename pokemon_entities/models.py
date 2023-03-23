from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)

    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)

    # def __str__(self):
    #     return '{}'.format(self.lat, self.lon)
