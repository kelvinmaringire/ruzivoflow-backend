from django.contrib.auth.models import User, Group, Permission

from rest_framework import generics

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.backends import TokenBackend

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




