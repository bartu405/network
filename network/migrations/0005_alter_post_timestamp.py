# Generated by Django 4.1 on 2022-09-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.CharField(blank=True, default='bro', max_length=64),
        ),
    ]