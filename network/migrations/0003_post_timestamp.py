# Generated by Django 4.1 on 2022-09-11 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 12, 1, 59, 12, 172634)),
        ),
    ]
