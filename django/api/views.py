import io

import PIL
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Image
from .serializers import ImageSerializer, RotateSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=['post'])
    def rotate(self, request, pk=None):
        image = self.get_object()
        pil_image = PIL.Image.open(image.image)
        serializer = RotateSerializer(data=request.POST)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        pil_image.rotate(serializer.validated_data['degrees'])
        with io.BytesIO() as f:
            pil_image.save(f, format=pil_image.format)
        image = self.get_object()
        serializer = self.get_serializer(image)
        return Response(serializer.data)
