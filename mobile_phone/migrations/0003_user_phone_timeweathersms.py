# Generated by Django 2.2.4 on 2019-08-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_phone', '0002_user_phone_sendweathersms'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_phone',
            name='timeWeatherSMS',
            field=models.CharField(default='07:30', max_length=5),
            preserve_default=False,
        ),
    ]
