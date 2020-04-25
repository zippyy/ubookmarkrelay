# Generated by Django 3.0.5 on 2020-04-25 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ubookmark', '0002_bookmarkmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarkmodel',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
