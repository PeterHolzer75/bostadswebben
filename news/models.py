from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, TextField
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks


# Create your models here.

# https://www.youtube.com/watch?v=6YrbkE0_RPQ&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=16
# 5: 58


class NewsListingPage(Page):
    """ listar alla nyhetsinlägg """
    template = "news/news_listing_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Overwrites the default title",
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['news'] = NewsDetailPage.objects.live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),

    ]


class NewsDetailPage(Page):

    # custom_title = models.CharField(
    #     max_length=100,
    #     blank=True,
    #     null=True,
    #     help_text="Overwrites the default title",

    # )

    ingress = StreamField(

        [
            ("simple_richtext", blocks.SimpleRichtextBlock(
                classname="simple-richtext")),
        ],
        null=True,
        blank=True

    )

    news_image = models.ForeignKey("wagtailimages.Image",
                                   blank=False,
                                   null=True,
                                   related_name="+",
                                   on_delete=models.SET_NULL,


                                   )

    content = StreamField(

        [
            ("title_and_text", blocks.TitleAndTextBlock(classname="text-and-title")),
            ("full_richtext", blocks.RichtextBlock(classname="richtext-full")),
            ("simple_richtext", blocks.SimpleRichtextBlock(
                classname="richtext-simple")),


        ],
        null=True,
        blank=True

    )

    content_panels = Page.content_panels + [
        # FieldPanel('custom_title'),
        StreamFieldPanel("ingress"),
        StreamFieldPanel("content"),
        ImageChooserPanel('news_image'),

    ]
