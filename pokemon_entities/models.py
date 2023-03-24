from django.db import models  # noqa F401


class MyModel(models.Model):
    objects = models.Manager()


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Имя на английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя на японском')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='pokemons', blank=True, verbose_name='Картинка')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child',
                               verbose_name='Из кого эволюционировал')


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, verbose_name='Дата и время появления')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Дата и время исчезновения')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

