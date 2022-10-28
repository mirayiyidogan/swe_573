from unicodedata import category
from unittest.util import _MAX_LENGTH


from django.db import models
from autoslug import AutoSlugField

class ContentModel(models.Model):
    name = models.CharField(max_length=50 , blank=False, null= False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table= 'content'
        verbose_name_plural = "Contents"
        verbose_name = "Content"

    def __str__(self):
        return self.name
