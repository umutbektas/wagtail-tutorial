"""StreamFields live in here"""


from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""
    title = blocks.CharBlock(required=True, help_text="Add Title")
    text = blocks.TextBlock(required=True, help_text="Additional Text")


    class Meta: # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"