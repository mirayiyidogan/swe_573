from django.db import models
from django.contrib.auth.models import User
from gotya.models import ContentModel

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    content = models.ForeignKey(ContentModel, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    class Meta:
        db_table= 'comment'
        verbose_name_plural = "Comments"
        verbose_name = "Comment"

    def __str__(self):
        return self.user.username
