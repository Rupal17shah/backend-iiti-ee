# Generated by Django 4.1.5 on 2023-04-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="semester",
            field=models.IntegerField(),
        ),
    ]
