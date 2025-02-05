# Generated by Django 3.1.8 on 2021-05-26 21:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubdate', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(default='The Ubyssey Magazine', max_length=100)),
                ('description', models.CharField(default='The Ubyssey Magazine', max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m')),
                ('social_cover_image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='MagazineSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(default='Magazine Section', max_length=100)),
                ('section_image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.magazineissue')),
            ],
        ),
    ]
