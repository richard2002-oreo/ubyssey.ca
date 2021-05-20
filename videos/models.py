from .validators import validate_youtube_url
from django.db import models
from django.utils import timezone

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

#-----Orderable models-----

class VideoAuthorsOrderable(Orderable):
    """
    This closely corresponds to the Dispatch model that is (mis-)named "Author"
    """
    video = ParentalKey(
        "videos.VideoSnippet",
        related_name="video_authors",
    )
    author = models.ForeignKey(
        'authors.AuthorSnippet',
        on_delete=models.CASCADE,
    )
    # author_role = CharField(        
    #     # While stored as a CharField, will be selected from a menu. See the Widget in the panels value of this Orderable
    #     max_length=50,
    #     null=False,
    #     blank=True,
    #     default='',
    # )
    panels = [
        MultiFieldPanel(
            [
                SnippetChooserPanel("author"),
                # FieldPanel(
                #     "author_role",
                #     widget=Select(
                #         choices=[
                #             ('', ''), 
                #             ('author', 'Author'), 
                #             ('illustrator','Illustrator'),
                #             ('photographer','Photographer'),
                #             ('videographer','Videographer'),
                #         ],
                #     ),
                # ),
            ],
            heading="Author",
        ),
    ]

#-----Snippet models-----

@register_snippet
class VideoSnippet(ClusterableModel):
    slug = models.SlugField(
        max_length=255,
        primary_key=True,
        unique=True,
        db_index=True,
        null=False,
        blank=False,
        default='',
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    url = models.URLField(
        max_length=500,
        null=False,
        blank=False,
        default='',
        validators=[validate_youtube_url,]
    )

    # authors = ManyToManyField(Author, related_name='video_authors')
    # tags = ManyToManyField('Tag')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("title"),
                FieldPanel("url"),
            ],
            heading="Necessary Fields"
        ),
        MultiFieldPanel(
            [
                InlinePanel("video_authors", max_num=20, label="Author"),
            ],
            heading="Author(s)"
        ),
    ]
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
