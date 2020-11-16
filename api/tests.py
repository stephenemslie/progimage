from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class ApiTests(APITestCase):

    def test_upload_image_required(self):
        """Test that image field is required"""
        url = reverse('image-list')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data["image"]), 1)
