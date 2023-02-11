from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Director(models.Model):
    first_name=models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    director_email=models.EmailField(verbose_name='Эл. почта')

    def get_url(self):
        return reverse('directors_info', args=[self.id])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'


    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name=models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')

    gender = models.CharField(max_length=1,choices=GENDERS, default=MALE, verbose_name='Пол')

    def get_url(self):
        return reverse('actors_info', args=[self.id])



    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер - {self.first_name} {self.last_name}'
        return f'Актриса - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]


    name = models.CharField(max_length=40, verbose_name='название')
    reting = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)],verbose_name='Рейтинг')
    year = models.IntegerField(null=True,blank=True, verbose_name='Год')
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)],verbose_name='Бюджет')
    currency=models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB,verbose_name='Валюта')
    slug= models.SlugField(default='', null=False, db_index=True)

    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, verbose_name='Режиссер', related_name='movies')
    actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='movies')

    #def save(self, *args, **kwargs):
        #self.slug = slugify(self.name)
       # super(Movie, self).save(*args,**kwargs)

    def get_url(self):
        return reverse('movie-detail',args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.reting}%'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


#python manage.py shell_plus --print-sql