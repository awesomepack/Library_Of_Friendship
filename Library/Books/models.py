from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=25)
    ISBN = models.IntegerField( primary_key=True)
    pub_date = models.DateField("Date Published")
    Image = models.ImageField("Book Cover")
    Summary = models.CharField(max_length= 500)
