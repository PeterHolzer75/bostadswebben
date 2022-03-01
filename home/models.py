from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePageCarouselImages(Orderable):
    """ Between 1 and 5 images for the homepage carousel"""
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    image_title = models.CharField(max_length=100, blank=False, null=True)
    image_subtitle = RichTextField(
        features=["bold", "italic"], null=True, blank=True)
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False, on_delete=models.SET_NULL, related_name="+"
    )

    panels = [ImageChooserPanel("carousel_image"),
              FieldPanel("image_title"),
              FieldPanel("image_subtitle")
              ]


class HomePage(Page):
    """ Home page model """
    templates = "home/home_page.html"
    max_count = 1  # det kan bara finnas en enda Homepage (single Site)

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(

        "wagtailimages.Image",
        null=True, blank=False, on_delete=models.SET_NULL, related_name="+"
    )
    banner_cta = models.ForeignKey(

        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+")

    # Content Panels ----------------------------------------------------------------------
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel("carousel_images", min_num=1, max_num=5, label="Image")
        ], heading="Carouselbilder"),
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="Banner options"),

    ]

    class Meta:
        verbose_name = "Startsida (Homepage)"
        verbose_name_plural = "Startsidor"
