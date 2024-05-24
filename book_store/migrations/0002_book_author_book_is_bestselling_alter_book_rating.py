# Generated by Django 5.0.6 on 2024-05-24 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="is_bestselling",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]
