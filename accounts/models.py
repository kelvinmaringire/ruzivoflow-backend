from django.db import models

from wagtail.snippets.models import register_snippet

@register_snippet
class ContactForm(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
