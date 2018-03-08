from django.contrib import admin
from .models import writer, book
# Register your models here.



#admin.site.register(Country)



@admin.register(writer)
class Writerdmin(admin.ModelAdmin):

    list_display = ('writer_name', 'writer_dob', 'writer_dod','writer_contact','writer_bio','writer_image')
    fields = ['writer_name','writer_dob', 'writer_dod','writer_contact','writer_bio','writer_image']



@admin.register(book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('book_name', 'book_pubdate','book_summary')




