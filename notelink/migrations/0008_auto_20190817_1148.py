# Generated by Django 2.2.4 on 2019-08-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notelink', '0007_auto_20190415_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='noteTimestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
