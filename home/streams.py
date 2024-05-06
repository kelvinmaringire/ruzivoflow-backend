from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ServicesBlock(blocks.StructBlock):
    icon = blocks.CharBlock()
    title = blocks.CharBlock()
    subtitle = blocks.RichTextBlock()