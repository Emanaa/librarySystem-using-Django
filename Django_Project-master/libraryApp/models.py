from audioop import reverse
from django.contrib.auth.models import User
from django.db import models
from datetime import date


class writer(models.Model):
   writer_id=models.AutoField(primary_key=True)
   writer_name=models.CharField(max_length=100)
   writer_dob=models.DateField()
   writer_dod=models.DateField('died',null=True, blank=True)
   writer_contact=models.CharField(max_length=100)
   writer_bio=models.TextField()
   writer_image=models.ImageField(upload_to='static/images', blank=True)
   def __str__(self):
       return self.name

class book(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=100)
    book_pubdate=models.DateField()
    book_summary=models.TextField()
    book_country=models.CharField(max_length=100)
    book_link=models.CharField(max_length=100)
    bwriter_id=models.ForeignKey('writer', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
