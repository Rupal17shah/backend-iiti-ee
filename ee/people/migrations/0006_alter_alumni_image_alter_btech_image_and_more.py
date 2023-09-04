# Generated by Django 4.1.5 on 2023-04-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0005_alter_alumni_image_alter_btech_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="btech",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="faculty",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="mtech",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="phd",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="staff",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]