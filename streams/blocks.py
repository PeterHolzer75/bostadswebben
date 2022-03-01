"""StreamField livres here"""
import mmap
# from cProfile import label
from email.policy import default
# from mmap import MAP_EXECUTABLE
import re
# from typing_extensions import Required
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class GalleryBlock(blocks.StructBlock):
    """ Gallary wityh title and images """

    title = blocks.CharBlock(required=True, help_text="ange titel")

    gallery = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),

            ]))

    class Meta:
        template = "streams/gallery_block.html"
        icon = 'image'
        label = 'Galleri'


class TextBlock(blocks.StructBlock):

    text = blocks.TextBlock(required=True)

    class Meta:
        template = "streams/text_block.html"
        icon = "edit"
        label = "Textblock"


class ImageBlock(blocks.StructBlock):
    """ Only 1 image """

    image = ImageChooserBlock(required=True)

    class Meta:
        template = "streams/image_block.html"
        icon = 'placeholder'
        label = 'Image'

# class ImageBlock(blocks.StructBlock):
#     """ Only images """

#     images = blocks.ListBlock(
#         blocks.StructBlock(
#             [
#                 ("image", ImageChooserBlock(required=True)),

#             ]))

#     class Meta:
#         template = "streams/image_block.html"
#         icon = 'placeholder'
#         label = 'Images'


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="ange titel")
    text = blocks.TextBlock(required=True, help_text='ange mer text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Titel & Text"


class TitleAndRichtextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="ange titel")
    text = blocks.RichTextBlock(required=True, help_text='ange mer text')

    class Meta:
        template = "streams/title_and_richtext_block.html"
        icon = "edit"
        label = "Titel & Richtext"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all features"""
    class Meta:
        template = "streams/richtext_block.html"
        icon = 'doc-full'
        label = 'Richtext'

# https://www.youtube.com/watch?v=FJ3j-jfHTjg&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=9


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link", ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = 'edit'
        label = 'Richtext simple'

# https://www.youtube.com/watch?v=DMP-GcElEIo&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=10


class CardBlock(blocks.StructBlock):
    """ Cards with an image, text and button(s) """

    title = blocks.CharBlock(required=True, help_text="ange titel")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                 help_text='If the button above is selected, that will be used first.')),

            ]))

    class Meta:
        template = "streams/card_block.html"
        icon = 'placeholder'
        label = 'Personalkort'


class CTABlock(blocks.StructBlock):
    """Simple call to action section """

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(
        required=True, default='Lear more', max_length=40)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call To Action"
