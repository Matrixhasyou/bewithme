# Generated by Django 2.0.2 on 2018-03-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180317_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteitems',
            name='notification_text',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='notification',
            name='not_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='notification',
            name='start_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='notification_text',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
