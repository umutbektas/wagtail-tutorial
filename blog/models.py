from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.snippets.models import register_snippet

from streams import blocks


class BlogAuthor(models.Model):
    """Blog author for snippets"""
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("image"),
            ],
            heading="Name and Image"
        ),
        MultiFieldPanel(
            [
                FieldPanel("website")
            ],
            heading="Links"
        )
    ]

    def __str__(self):
        """String repr of this class."""
        return self.name

    class Meta: # noqa
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"


register_snippet(BlogAuthor)


class BlogListingPage(RoutablePageMixin, Page):
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
        context['sub_link'] = self.reverse_subpage('latest_posts')

        return context

    class Meta: # noqa
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Page"

    @route('^latest/$', name="latest_posts")
    def latest_blog_posts(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['posts'] = context['posts'][:2]

        return render(request, "blog/blog_latest_posts.html", context)

    def get_sitemap_urls(self, request):
        # uncoment to have no sitemap for this page
        # return []
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
                "location": self.full_url + self.reverse_subpage("latest_posts"), # route name
                "lastmod": (self.last_published_at or self.latest_revision_created_at),
                "priority": 0.9,
            }
        )
        return sitemap


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
