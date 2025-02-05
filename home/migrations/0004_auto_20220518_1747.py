# Generated by Django 3.2.11 on 2022-05-19 00:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210826_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='above_cut_stream',
            field=wagtail.core.fields.StreamField([('above_cut_block', wagtail.core.blocks.StructBlock([]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sections_stream',
            field=wagtail.core.fields.StreamField([('home_page_section_block', wagtail.core.blocks.StructBlock([('section', wagtail.core.blocks.PageChooserBlock(page_type=['section.SectionPage'])), ('layout', wagtail.core.blocks.ChoiceBlock(choices=[('news', '"News Section" Style'), ('featured', '"Featured Section" Style')]))]))], blank=True, null=True),
        ),
    ]
