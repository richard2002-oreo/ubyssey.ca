# Generated by Django 3.1.12 on 2021-07-09 10:44

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields
import ubyssey.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsTournamentSnippet',
            fields=[
                ('tournament_name', models.TextField(default='tournament')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='tournament_name', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Sports Tournament',
                'verbose_name_plural': 'Sports Tournaments',
            },
        ),
        migrations.CreateModel(
            name='SportsTeamOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('team_name', models.TextField(default='')),
                ('team_color', models.CharField(default='#FF0000', max_length=7, validators=[ubyssey.validators.validate_colour_hex])),
                ('team_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('tournament', modelcluster.fields.ParentalKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tournament_team', to='sporttourney.sportstournamentsnippet')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SportsPlayerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('profile_text', models.CharField(blank=True, max_length=1500)),
                ('player_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]
