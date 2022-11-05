from atexit import register
from django import template
from gotya.models import CategoryModel

register = template.Library()

@register.simple_tag
def categories_list():
    categories = CategoryModel.objects.all()
    return categories