# Generated by Django 3.1.12 on 2021-07-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20210714_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='legacy_template',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
    ]
