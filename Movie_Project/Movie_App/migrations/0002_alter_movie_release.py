# Generated by Django 5.0.2 on 2024-02-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release',
            field=models.DateField(),
        ),
    ]
