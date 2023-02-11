from django.contrib import admin, messages
from .models import Movie, Director, Actor
from django.db.models import QuerySet
# Register your models here.


admin.site.register(Director)
#@admin.register(Director)
#class DirecrotAdmin(admin.ModelAdmin):
    #list_display = ['first_name', 'last_name', 'director_email']

admin.site.register(Actor)

class RatingFilter(admin.SimpleListFilter):

    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('< 40', 'Низкий рейтинг'),
            ('от 40 до 59', 'Средний рейтинг'),
            ('от 60 до 79', 'Высокий рейтинг'),
            ('>= 80', 'Высочайший рейтинг')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value()=='< 40':
            return queryset.filter(reting__lt=40)
        if self.value()=='от 40 до 59':
            return queryset.filter(reting__gte=40).filter(reting__lt=60)
        if self.value()=='от 60 до 79':
            return queryset.filter(reting__gte=60).filter(reting__lt=79)
        if self.value()=='>= 80':
            return queryset.filter(reting__gte=80)
        return queryset



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ['name','reting']
    #exclude = ['slug']
    #readonly_fields = ['year']

    prepopulated_fields = {'slug':('name',)}

    list_display = ['name','reting','currency','budget','director', 'rating_status']
    list_editable = ['reting','currency','budget','director']
    ordering = ['-reting', 'name']
    #list_per_page = 3
    actions = ['set_dollars','set_euro']
    search_fields = ['name','reting']
    list_filter = ['name','currency',RatingFilter]

    filter_horizontal = ['actors']

    @admin.display(ordering='reting', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.reting < 50:
            return 'Зачем это смотреть?'
        if mov.reting < 70:
            return 'Разок можно глянуть'
        if mov.reting <= 85:
            return 'Зачет'
        return 'Топ контент'


    @admin.action(description='Установить валюту в - Доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в - Евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            #messages.ERROR
        )