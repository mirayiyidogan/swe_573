# Generated by Django 4.1.2 on 2022-10-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotya', '0005_rename_create_date_contentmodel_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmodel',
            name='tags',
            field=models.ManyToManyField(related_name='content', to='gotya.tagmodel'),
        ),
    ]
