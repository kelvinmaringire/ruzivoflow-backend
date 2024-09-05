import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from treebeard.mp_tree import MP_Node


@register_snippet
class NodeCategory(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("icon"),
        FieldPanel("description")
    ]


@register_snippet
class Node(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey(NodeCategory, on_delete=models.SET_NULL, null=True)
    html_id = models.CharField(max_length=15)
    type = models.CharField(max_length=20)
    icon = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("category"),
        FieldPanel("html_id"),
        FieldPanel("type"),
        FieldPanel("icon"),
        FieldPanel("order")
    ]

    class Meta:
        ordering = ['order', 'name']


@register_snippet
class Workflow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("user"),
        FieldPanel("description")
    ]


@register_snippet
class NodeItem(MP_Node):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    original_name = models.CharField(max_length=15)
    filename = models.CharField(max_length=40, null=True)
    original_id = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    html_id = models.CharField(max_length=30)
    icon = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=20)
    data_type = models.CharField(max_length=20, null=True)
    style_object = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    formData = models.JSONField(null=True, blank=True)
    edited = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    node_order_by = ['name']

    def __str__(self):
        return self.original_id

    panels = [
        FieldPanel("name")
    ]

    def delete(self, *args, **kwargs):
        if self.filename:
            file_path = os.path.join(settings.BASE_DIR, "mixins", "files", self.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        super(NodeItem, self).delete(*args, **kwargs)


@register_snippet
class Connection(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    sourceId = models.CharField(max_length=30)
    targetId = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.sourceId} -> {self.targetId}'

    panels = [
        FieldPanel("workflow")
    ]


