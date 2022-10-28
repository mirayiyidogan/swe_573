from pyexpat import model
from django.db import models
from autoslug import AutoSlugField

class TextModel(models.Model):
    header = models.CharField(max_lenght=50)
    text= models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from= "header", unique= True)

