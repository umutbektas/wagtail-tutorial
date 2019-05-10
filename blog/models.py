from django.db import models

from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks



class BlogListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "blog/blog_listing_page.html"

    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="Overwrites the Default Title")

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogDetailPage.objects.live().public()

        return context


    class Meta: # noqa
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Page"



class BlogDetailPage(Page):
    """Blog detail page."""

    template = "blog/blog_detail_page.html"

    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="Overwrites the Default Title")
    blog_image = models.ForeignKey("wagtailimages.Image", blank=False, null=True, related_name="+", on_delete=models.SET_NULL)


    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]


    class Meta: # noqa
        verbose_name = "Post"
        verbose_name_plural = "Posts"
