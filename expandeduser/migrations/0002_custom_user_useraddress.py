# Generated by Django 2.2.4 on 2019-08-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expandeduser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='userAddress',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]