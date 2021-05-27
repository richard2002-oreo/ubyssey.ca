# Generated by Django 3.1.8 on 2021-05-27 02:00

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('article', '0002_auto_20210526_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='article.articlepage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_articlepagetag_items', to='taggit.tag')),
            ],
            options={
                'verbose_name': 'article tag',
                'verbose_name_plural': 'article tags',
            },
        ),
        migrations.AddField(
            model_name='articlepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='article.ArticlePageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
