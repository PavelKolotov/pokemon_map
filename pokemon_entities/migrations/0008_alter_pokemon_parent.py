# Generated by Django 4.1.7 on 2023-03-24 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_pokemon_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал'),
        ),
    ]
