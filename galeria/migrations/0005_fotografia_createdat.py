# Generated by Django 5.0.1 on 2024-01-28 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
