# Generated by Django 4.1 on 2022-09-13 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_remove_like_liker_like_liker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
