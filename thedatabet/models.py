from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.documents import get_document_model


@register_snippet
class BettingTips(models.Model):
    date = models.DateField()
    tips = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("date"),
        FieldPanel("tips")
    ]
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")



class TheDataBet(Page):
    betting_tips = models.ForeignKey(
        'thedatabet.BettingTips',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('betting_tips'),  # This creates the dropdown
    ]