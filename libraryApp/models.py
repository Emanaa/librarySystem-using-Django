from audioop import reverse
from django.contrib.auth.models import User
from django.db import model
from datetime import date


class writer(models.Model):
   writer_id=models.AutoField(primary_ket=true);
   writer_name=models.models.CharField(max_length=100);
   writer_dob=models.DateField();
   writer_dod=models.DateField('died',null=True, blank=True);
   writer_contact=models.CharField(max_length=100);
   writer_bio=models.TextField();
   writer_image=models.ImageField(upload_to='static/images', blank=True);
   def __str__(self):
       return self.name

class book(models.Model):
    book_id=models.AutoField(primary_ket=true);
    book_name=models.models.CharField(max_length=100);
    book_pubdate=models.DateField();
    book_summary=models.TextField();
    book_country=models.CharField(max_length=100);
    book_link=models.CharField(max_length=100);
    bwriter_id=models.ForeignKey('writer', on_delete=models.CASCADE);
    def __str__(self):
        return self.name
# Create your models here.
#class Country(models.Model):
    """
    Model representing a Country (e.g. london, France, Japan, etc.)
    """
  #  name = models.CharField(max_length=200,
   #                         help_text="Enter a the country's natural language (e.g. london, France, Japan, etc.)")

    #def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
     #  return self.name


#class Book(models.Model):
    """
    Model representing a book .
    """
 #   title = models.CharField(max_length=200)
  #  publishedAt = models.DateField(null=True, blank=True)

   # summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")

    #country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    #link = models.CharField(max_length=200, help_text="Enter a link of the book")
    #writer = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True)

    #def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        #return reverse('book-detail', args=[str(self.id)])

    #def __str__(self):
        """
        String for representing the Model object.
        """
      #  return self.title


#class Writer(models.Model):
    """
    Model representing an writer.
    """
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_death= models.DateField('died', null=True, blank=True)
    #contact = models.CharField(max_length=100)

    #books = models.CharField(max_length=100, help_text="enter books here ")
    #bio = models.ImageField(upload_to='pictures', blank=True)

    #class Meta:
    #    ordering = ["first_name", "last_name"]

    #def get_absolute_url(self):
        """
        Returns the url to access a particular writer instance.
        """
     #   return reverse('writer-detail', args=[str(self.id)])

    #def __str__(self):
        """
        String for representing the Model object.
        """
       # return '{0}{1}'.format(self.first_name, self.last_name)
