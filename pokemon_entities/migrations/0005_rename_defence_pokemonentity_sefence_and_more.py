# Generated by Django 4.1.7 on 2023-03-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_mymodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Defence',
            new_name='sefence',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Stamina',
            new_name='stamina',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Strength',
            new_name='strength',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]