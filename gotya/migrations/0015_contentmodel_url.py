# Generated by Django 4.1.2 on 2022-12-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotya', '0014_rename_tagmodel_categorymodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmodel',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
