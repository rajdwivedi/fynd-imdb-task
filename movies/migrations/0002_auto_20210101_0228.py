# Generated by Django 3.0.3 on 2020-12-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(),
        ),
    ]
