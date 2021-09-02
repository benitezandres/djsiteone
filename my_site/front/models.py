from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state_province = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=45)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()