from django.contrib.auth.models import User, Group, Permission
from django.core.mail import send_mail

from rest_framework import generics

from .models import ExtendedUser, ContactForm
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer, ExtendedUserSerializer, ContactFormSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class ExtendedUserListCreate(generics.ListCreateAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer


class ExtendedUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer


class ContactFormListCreate(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        contact = serializer.save()  # Save the form data to the database

        # Prepare and send email
        subject = f"New Contact Message from {contact.fullname}"
        message = f"""
    You have received a new contact message:

    From: {contact.fullname}
    Email: {contact.email}

    Message:
    {contact.message}
    """
        send_mail(
            subject=subject,
            message=message,
            from_email=contact.email,
            recipient_list=['kelvinmaringire@gmail.com'],
            fail_silently=False,
        )




