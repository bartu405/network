# Generated by Django 4.1 on 2023-05-04 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0062_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 0, 33, 47, 213832)),
        ),
    ]
