# Generated by Django 2.2.4 on 2019-08-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_phone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_phone',
            name='sendWeatherSMS',
            field=models.BooleanField(default=False),
        ),
    ]
