from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Author(models.Model):
    '''The Author of the Books'''

    Name = models.CharField(max_length= 50)

    def __str__(self):
        return self.Name

class Book(models.Model):
    '''Book information'''
    Name = models.CharField(max_length=25)
    ISBN = models.IntegerField( primary_key=True)
    pub_date = models.DateField("Date Published")
    Image = models.ImageField("Book Cover")
    Summary = models.CharField(max_length= 500)
    Author_id = models.ForeignKey(Author , on_delete= models.CASCADE , default= None)

    def __str__(self):
        return self.Name
    
    def Book_Title_Length(self):
        return len(self.Name)
    
    '''To Do:
    Delete my current Book object > Delete my current Author Object > Create an Author object > Create a Book object using Book.set.create()'''
    



    