# Generated by Django 4.1.2 on 2022-10-29 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gotya', '0009_alter_contentmodel_text_commentmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
