# Generated by Django 4.1 on 2022-09-12 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_user_followers_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
    ]