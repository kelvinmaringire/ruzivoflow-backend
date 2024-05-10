from wagtail import blocks


class ServicesBlock(blocks.StructBlock):
    icon = blocks.CharBlock()
    title = blocks.CharBlock()
    subtitle = blocks.RichTextBlock()