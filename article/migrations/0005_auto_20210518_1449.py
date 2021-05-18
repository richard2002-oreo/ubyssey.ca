# Generated by Django 3.1.8 on 2021-05-18 21:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20210503_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(help_text='Write your article contents here. See documentation: https://docs.wagtail.io/en/latest/editor_manual/new_pages/creating_body_content.html#rich-text-fields', label='Rich Text Block')), ('plaintext', wagtail.core.blocks.TextBlock(help_text='Warning: Rich Text Blocks preferred! Plain text primarily exists for importing old Dispatch text.', label='Plain Text Block')), ('dropcap', wagtail.core.blocks.TextBlock(help_text='Create a block where special dropcap styling with be applied to the first letter and the first letter only.\n\nThe contents of this block will be enclosed in a <p class="drop-cap">...</p> element, allowing its targetting for styling.\n\nNo RichText allowed.', label='Dropcap Block', template='article/stream_blocks/dropcap.html')), ('pagebreak', wagtail.core.blocks.static_block.StaticBlock(label='Pagebreak - USE RICHTEXT INSTEAD', template='article/stream_blocks/pagebreak.html')), ('video', wagtail.core.blocks.StructBlock([('video_embed', wagtail.embeds.blocks.EmbedBlock(blank=False, null=False)), ('tile', wagtail.core.blocks.CharBlock()), ('caption', wagtail.core.blocks.CharBlock()), ('credit', wagtail.core.blocks.CharBlock())], label='Video Block', template='article/stream_blocks/video.html')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))], blank=True, null=True),
        ),
    ]
