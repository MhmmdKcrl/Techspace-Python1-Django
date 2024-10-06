# Generated by Django 4.2.11 on 2024-10-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="name_az",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_ru",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="description_az",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="description_ru",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="title_az",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="title_en",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="title_ru",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="tags",
            name="name_az",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="tags",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="tags",
            name="name_ru",
            field=models.CharField(max_length=50, null=True),
        ),
    ]