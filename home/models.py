from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.api import APIField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel, FieldRowPanel

from .streams import ServicesBlock


class HomePage(Page):
    hero_title = models.CharField(max_length=100, blank=False, null=True)
    hero_subtitle = RichTextField(null=True, blank=False)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_outline_button_title = models.CharField(max_length=100, blank=False, null=True)
    hero_outline_button_url = models.CharField(null=True, blank=False)
    hero_flat_button_title = models.CharField(max_length=100, blank=False, null=True)
    hero_flat_button_url = models.CharField(null=True, blank=False)

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
            FieldPanel("hero_title"),
            FieldPanel("hero_subtitle"),
            FieldPanel("hero_image"),
            FieldPanel("hero_outline_button_title"),
            PageChooserPanel("hero_outline_button_url"),
            FieldPanel("hero_flat_button_title"),
            FieldPanel("hero_flat_button_url"),
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
        APIField('hero_title'),
        APIField('hero_subtitle'),
        APIField('hero_image'),
        APIField('hero_outline_button_title'),
        APIField('hero_outline_button_url'),
        APIField('hero_flat_button_title'),
        APIField('hero_flat_button_url'),
        APIField('services_title'),
        APIField('services'),
        APIField('landing_page_title'),
        APIField('landing_page_box_title'),
        APIField('landing_page_box_subtitle'),
        APIField('landing_page_image'),

    ]