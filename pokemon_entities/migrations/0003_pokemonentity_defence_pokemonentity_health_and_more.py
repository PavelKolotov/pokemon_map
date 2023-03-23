# Generated by Django 4.1.7 on 2023-03-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemonentity_appeared_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Health',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(null=True),
        ),
    ]
