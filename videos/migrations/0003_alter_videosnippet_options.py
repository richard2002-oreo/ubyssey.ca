# Generated by Django 3.2.11 on 2022-01-30 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videospage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videosnippet',
            options={'ordering': ['-created_at'], 'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]
