from django.contrib import admin
from .models import Writer, Book,Country
# Register your models here.



admin.site.register(Country)



@admin.register(Writer)
class Writerdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death','contact','books','bio')
    fields = ['first_name', 'last_name','date_of_birth', 'date_of_death','contact','books','bio']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'publishedAt','country','writer')





