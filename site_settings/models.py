from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    """ Sicial media settimgs for bostadswebben """

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    instagram = models.URLField(
        blank=True, null=True, help_text="Instragram URL")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")
    youtube = models.URLField(blank=True, null=True,
                              help_text="Youtube Channel URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("linkedin"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]
