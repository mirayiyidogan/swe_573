from django.db import models
from autoslug import AutoSlugField
from gotya.models import CategoryModel
from django.contrib.auth.models import User
from gotya.abstract_models import DateAbstractModel
from ckeditor.fields import RichTextField

class ContentModel(DateAbstractModel):
    header = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="content_pics")
    url = models.CharField(max_length=200, blank=True)
    text = RichTextField(blank=True)
    slug = AutoSlugField(populate_from= "header", unique= True)
    CategoryModels = models.ManyToManyField(CategoryModel, related_name="content")
    user = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name="contents") #If a user will be deleted, on_delete will also deletes its contents

    class Meta:
        db_table= 'content'
        verbose_name_plural = "Contents"
        verbose_name = "Content"

    def __str__(self):
        return self.header


