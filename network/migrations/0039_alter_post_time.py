# Generated by Django 4.1 on 2023-01-23 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0038_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 23, 19, 2, 13, 212410)),
        ),
    ]
