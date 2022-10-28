# Generated by Django 4.1.2 on 2022-10-28 17:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gotya', '0008_alter_contentmodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmodel',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gotya.contentmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commnet',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment',
            },
        ),
    ]
