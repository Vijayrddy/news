# Generated by Django 3.2.6 on 2022-01-15 23:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=400),
        ),
    ]
