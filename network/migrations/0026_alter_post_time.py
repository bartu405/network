# Generated by Django 4.1 on 2022-09-14 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0025_alter_followers_followers_alter_following_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 4, 1, 14, 59654)),
        ),
    ]
