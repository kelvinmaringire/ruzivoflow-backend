from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class BettingTips(models.Model):
    date = models.DateField()
    games = models.JSONField()
    host_sc_mse = models.FloatField()
    host_sc_r2 = models.FloatField()
    guest_sc_mse = models.FloatField()
    guest_sc_r2 = models.FloatField()
    result_mse = models.FloatField()
    result_r2 = models.FloatField()

    panels = [
        FieldPanel("date")
    ]

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
