# Generated by Django 5.0.1 on 2024-01-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
