from django.db import models
from django.contrib.auth.models import User

from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet


@register_snippet
class ExtendedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cell_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Physical address')
    sex = models.CharField(max_length=10, null=True)
    dob = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    pic = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_query_name='user_pic')
    company_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

@register_snippet
class ContactForm(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
