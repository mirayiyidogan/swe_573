from django.db import models
from autoslug import AutoSlugField
from gotya.models import TagModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class ContentModel(models.Model):
    header = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="content_pics")
    text = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from= "header", unique= True)
    tags = models.ManyToManyField(TagModel, related_name="content")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contents") #If a user will be deleted, on_delete will also deletes its contents

    class Meta:
        db_table= 'content'
        verbose_name_plural = "Contents"
        verbose_name = "Content"

    def __str__(self):
        return self.header


