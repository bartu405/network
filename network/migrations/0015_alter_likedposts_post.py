# Generated by Django 4.1 on 2022-09-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_likedposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedposts',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, to='network.post'),
        ),
    ]
