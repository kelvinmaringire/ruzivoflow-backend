import json
from django.db import models
from django.core.exceptions import ValidationError
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.documents import get_document_model


@register_snippet
class BettingTips(models.Model):
    date = models.DateField()
    file = models.ForeignKey(
        get_document_model(),
        on_delete=models.CASCADE,
        null=True
    )
    json_data = models.JSONField(blank=True, null=True)

    panels = [
        FieldPanel("date"),
        FieldPanel("file"),
    ]

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

    def save(self, *args, **kwargs):
        if self.file and self.file.file:
            try:
                # Read and parse JSON from the uploaded file
                with self.file.file.open("r") as f:
                    data = json.load(f)
                    self.json_data = data  # Changed from self.tips to self.json_data
            except json.JSONDecodeError:
                raise ValidationError("Uploaded file is not a valid JSON.")
            except Exception as e:
                raise ValidationError(f"Error reading the file: {str(e)}")

        super().save(*args, **kwargs)
