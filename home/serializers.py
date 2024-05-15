from os.path import basename, splitext
from rest_framework.serializers import Field
from django.conf import settings


class ImageSerializedField(Field):
    def to_representation(self, value):
        request = self.context.get('request')
        filename, extension = splitext(value.file.name)
        filename_without_extension = basename(filename)
        return {
            "image": request.build_absolute_uri(value.file.url),
            "name": filename_without_extension
        }



