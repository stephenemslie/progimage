from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'created', 'image']


class RotateSerializer(serializers.Serializer):
    degrees = serializers.IntegerField()
