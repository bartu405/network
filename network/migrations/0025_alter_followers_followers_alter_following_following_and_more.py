# Generated by Django 4.1 on 2022-09-14 01:01

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0024_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 4, 1, 13, 498422)),
        ),
    ]
