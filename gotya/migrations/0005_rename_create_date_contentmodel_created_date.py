# Generated by Django 4.1.2 on 2022-10-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gotya', '0004_tagmodel_alter_contentmodel_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentmodel',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
