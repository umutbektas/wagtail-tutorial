"""StreamFields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""
    title = blocks.CharBlock(required=True, help_text="Add Title")
    text = blocks.TextBlock(required=True, help_text="Additional Text")


    class Meta: # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)"""
    title = blocks.CharBlock(required=True, help_text="Add Title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be use first.")),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"




class RichTextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta: #noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)

        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta: #noqa
        template = "streams/simple_richtext_block.html"
        icon = "edit"
        label = "Simple RichText"



class CTABlock(blocks.StructBlock):
    """A simple call to action section."""
    
    title = blocks.CharBlock(required=False, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False) # internal
    button_url = blocks.URLBlock(required=False) # external
    button_text = blocks.CharBlock(required=False, default="Learn More", max_length=30)

    class Meta: # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"



class LinkStructValue(blocks.StructValue):
    """Additional logic for urls"""
    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')

        if button_page:
            return button_page
        elif button_url:
            return button_url

        return None


class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""
    button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used first.") # internal
    button_url = blocks.URLBlock(required=False, help_text="If added, this url will be used secondarily.") # external   

    class Meta: # noqa
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue