from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.api import APIField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel, FieldRowPanel

from .streams import ServicesBlock


class HomePage(Page):
    heroTitle = models.CharField(max_length=100, blank=False, null=True)
    heroSubtitle = RichTextField(null=True, blank=False)
    heroImage = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    heroOutlineButtonTitle = models.CharField(max_length=100, blank=False, null=True)
    heroOutlineButtonHref = models.CharField(null=True, blank=False)
    heroFlatButtonTitle = models.CharField(max_length=100, blank=False, null=True)
    heroFlatButtonHref = models.CharField(null=True, blank=False)

    services_title = models.CharField(max_length=100, blank=False, null=True)
    services = StreamField([
        ('service', ServicesBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    landing_page_title = models.CharField(max_length=100, blank=False, null=True)
    landing_page_box_title = models.CharField(max_length=100, blank=False, null=True)
    landing_page_box_subtitle = RichTextField(null=True, blank=False)
    landing_page_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("heroTitle"),
            FieldPanel("heroSubtitle"),
            FieldPanel("heroImage"),
            FieldPanel("heroOutlineButtonTitle"),
            FieldPanel("heroOutlineButtonHref"),
            FieldPanel("heroFlatButtonTitle"),
            FieldPanel("heroFlatButtonHref"),
        ], heading="Hero Options", classname="collapsed", icon="desktop"),
        MultiFieldPanel([
            FieldPanel("services_title"),
            FieldPanel("services"),
        ], heading="Services", classname="collapsed", icon="cogs"),
        MultiFieldPanel([
            FieldPanel("landing_page_title"),
            FieldPanel("landing_page_box_title"),
            FieldPanel("landing_page_box_subtitle"),
            FieldPanel("landing_page_image"),
        ], heading="Landing Page", classname="collapsed", icon="image"),
    ]

    api_fields = [
        APIField('heroTitle'),
        APIField('heroSubtitle'),
        APIField('heroImage'),
        APIField('heroOutlineButtonTitle'),
        APIField('heroOutlineButtonHref'),
        APIField('heroFlatButtonTitle'),
        APIField('heroFlatButtonHref'),
        APIField('services_title'),
        APIField('services'),
        APIField('landing_page_title'),
        APIField('landing_page_box_title'),
        APIField('landing_page_box_subtitle'),
        APIField('landing_page_image'),

    ]