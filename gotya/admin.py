from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gotya.models import (
    ContentModel, TagModel, CommentModel, ContactModel
    )

admin.site.register(TagModel)


class ContentsAdmin(admin.ModelAdmin):
    search_fields= ("header", "text")
    list_display= (
        "header", "created_date", "edit_date"
    )

admin.site.register(ContentModel,ContentsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display= ('user', "created_date", "updated_date")
    search_field= ("comment_user")

admin.site.register(CommentModel, CommentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display= ('email', "created_date")
    search_field= ("email")

admin.site.register(ContactModel, ContactAdmin)