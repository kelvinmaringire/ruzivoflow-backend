from rest_framework import generics

from .models import ContactForm
from .serializers import ContactFormSerializer


class ContactFormListCreate(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

