# Generated by Django 4.1.4 on 2023-02-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_alter_actor_options_alter_director_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movie_app.actor', verbose_name='Актеры'),
        ),
    ]