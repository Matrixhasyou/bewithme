# Generated by Django 2.0.2 on 2018-03-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteitems',
            name='img_url',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='img_url',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
