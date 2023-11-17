# Generated by Django 4.0 on 2022-01-11 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='comments.comment'),
        ),
    ]
