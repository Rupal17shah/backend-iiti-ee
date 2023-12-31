# Generated by Django 4.1.5 on 2023-08-08 20:29

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_news_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="image",
        ),
        migrations.AddField(
            model_name="news",
            name="day",
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="news",
            name="month",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="news",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 8, 8, 20, 29, 13, 463854, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.TextField(max_length=100),
        ),
    ]
