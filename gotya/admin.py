from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gotya.models import (
    ContentModel, CategoryModel, CommentModel, ContactModel
    )

admin.site.register(CategoryModel)

@admin.register(ContentModel)
class ContentsAdmin(admin.ModelAdmin):
    search_fields= ("header", "text")
    list_display= (
        "header", "created_date", "updated_date"
    )

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('user', "created_date", "updated_date")
    search_field= ("comment_user")


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display= ('email', "created_date")
    search_field= ("email")

