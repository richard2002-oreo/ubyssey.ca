from django.db.models import fields
from wagtail.core import models

#-----Page models-----
class SectionablePage(models.Page):
    """
    Abstract class for pages. Allows a page to be aware of which section it belongs to, based on the structure of the site hierarchy.

    Pages in the site heirarchy tend to belong to a section.
    Sections correspond to child nodes of the HomePage that themselves have many children.
    Therefore all SectionablePages have built-in capacity to traverse backwards up the Page tree
    """
    is_creatable = False #no page should ever JUST be a sectionable page. This is an "abstract" page
    current_section = fields.CharField(
        max_length=255, #should contain the SLUG of the current section, not its name. Max length reflects max Wagtail slug length
        null=False,
        blank=True,
        default='',
    ) 

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["current_section"] = self.current_section
        return context

    def save(self, *args, **kwargs):
        """
        Ensures the page's current section is synced with its parents/ancestors
        Or else, if this is a section page, its section is itself
        """
        if self.current_section != self.slug:
            # saves ourselves some queries - the above situation should only ever obtain if we're in a section named after our current page
            ancestors_qs = self.get_ancestors()
            if len(ancestors_qs) == 2:
                # if there are exactly two ancestors (root, homepage), this must be a section page, so use its slug for current section
                # (slightly too magic - if possible improve on this solution - it's hard to know what all and only section pages have without being able to refer to that class!)
                self.current_section = self.slug
            else:
                # otherwise, we have some non-section page that should be able to learn what section it's in from its parent
                try:           
                    self.current_section = ancestors_qs.last().specific.current_section
                except Exception as e:
                    # This shouldn't ever be hit, but worst case scenario the current_section field's use with caching etc. can still work with "ERROR_SECTION"
                    self.current_section = 'ERROR_SECTION'

        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
