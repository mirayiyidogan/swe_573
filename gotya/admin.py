from django.contrib import admin
from gotya.models import ContentModel, TagModel

admin.site.register(TagModel)


class ContentsAdmin(admin.ModelAdmin):
    search_fields= ("header", "text")
    list_display= (
        "header", "created_date", "edit_date"
    )

admin.site.register(ContentModel,ContentsAdmin)