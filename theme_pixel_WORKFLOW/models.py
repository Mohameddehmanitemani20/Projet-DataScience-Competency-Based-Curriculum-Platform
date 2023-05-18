from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
import datetime
import os
from django import forms
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
from django.templatetags.custom_filters import *
class Foo(models.Model):
    bar = models.CharField(max_length=100)
    ratings = GenericRelation(Rating, related_query_name='foos')

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('brand/', filename)




class Item(models.Model):
    name = models.TextField(max_length=191)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    image_details= models.ImageField(upload_to=filepath, null=True, blank=True)
    description = models.CharField(max_length=500,default="")
    file = models.FileField(upload_to=filepath, null=True, blank=True)
    
   

   

    def average_rating(self) -> float:
        return Rating.objects.filter(item=self).aggregate(Avg("rating"))["rating__avg"] or 0

  
    


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.header}: {self.rating}"
