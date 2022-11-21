from django.db import models

class ContactModel(models.Model):
    email= models.EmailField(max_length=250)
    name = models.TextField(default='some_value' ,max_length=50)
    surname= models.TextField(max_length=50)
    message= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table= "contact"
        verbose_name_plural = "Contacts"
        verbose_name = "Contact"

        def __str__(self):
            return self.email
            
