# Generated by Django 4.1.2 on 2022-10-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotya', '0007_alter_contentmodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmodel',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]
