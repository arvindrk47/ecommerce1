# Generated by Django 4.2.7 on 2023-12-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
