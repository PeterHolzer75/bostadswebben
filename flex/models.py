from email.policy import default
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks

"""Flexible page """


class FlexPage(Page):
    template = 'flex/flex_page.html'

    content = StreamField(
        [
            ("text", blocks.TextBlock(classname="text")),
            ("title_and_text", blocks.TitleAndTextBlock(classname="text-and-title")),
            ("title_and_richtext", blocks.TitleAndRichtextBlock(
                classname="richtexttext-and-title")),
            ("full_richtext", blocks.RichtextBlock(classname="richtext-full")),
            ("simple_richtext", blocks.SimpleRichtextBlock(
                classname="richtext-simple")),
            ("image", blocks.ImageBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            ("gallery", blocks.GalleryBlock()),

        ],
        null=True,
        blank=True

    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel("content"),

    ]

    class Meta:
        verbose_name = "Flex Plage"
        verbose_name_plural = "Flex Plages"

# =================================================================================
# Sida med vänstermeny
# =================================================================================


class FlexPage_LeftMenu(Page):
    template = 'flex/flexpage_leftmenu.html'

    content = StreamField(
        [
            ("text", blocks.TextBlock(classname="text")),
            ("title_and_text", blocks.TitleAndTextBlock(classname="text-and-title")),
            ("title_and_richtext", blocks.TitleAndRichtextBlock(
                classname="richtexttext-and-title")),
            ("full_richtext", blocks.RichtextBlock(classname="richtext-full")),
            ("simple_richtext", blocks.SimpleRichtextBlock(
                classname="richtext-simple")),
            ("image", blocks.ImageBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            ("gallery", blocks.GalleryBlock()),

        ],
        null=True,
        blank=True

    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Plage w left menu"
        verbose_name_plural = "Flex Plages w left menu"
