from audioop import reverse

from django.db import models
from datetime import date

# Create your models here.
class Country(models.Model):
    """
    Model representing a Country (e.g. london, France, Japan, etc.)
    """
    name = models.CharField(max_length=200,
                            help_text="Enter a the country's natural language (e.g. london, France, Japan, etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book .
    """
    title = models.CharField(max_length=200)
    publishedAt = models.DateField(null=True, blank=True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")

    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    link = models.CharField(max_length=200, help_text="Enter a link of the book")
    writer = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class Writer(models.Model):
    """
    Model representing an writer.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death= models.DateField('died', null=True, blank=True)
    contact = models.CharField(max_length=100)

    books = models.CharField(max_length=100, help_text="enter books here ")
    bio = models.ImageField(upload_to='pictures', blank=True)

    class Meta:
        ordering = ["first_name", "last_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular writer instance.
        """
        return reverse('writer-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}{1}'.format(self.first_name, self.last_name)