# Generated by Django 4.1 on 2023-08-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0014_staff_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="MS",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("year", models.IntegerField()),
            ],
        ),
    ]
