import io

from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase
from rest_framework import status
import PIL


def get_test_image():
    image = PIL.Image.new('RGB', (100, 100))
    with io.BytesIO() as f:
        image.save(f, format='JPEG')
        image_file = SimpleUploadedFile(
            "image.jpg", f.getvalue(), content_type="image/jpeg")
    return image_file


class ImageTests(APITestCase):

    def test_upload_image_required(self):
        """Test that image field is required"""
        url = reverse('image-list')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data["image"]), 1)

    def test_upload_invalid_image(self):
        """Test that uploaded file is a valid image"""
        url = reverse('image-list')
        image_file = SimpleUploadedFile(
            "image.jpg", b"bad content", content_type="image/jpeg")
        data = {"image": image_file}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("Upload a valid image" in response.data["image"][0])

    def test_upload_valid_image(self):
        """Test uploading a valid image"""
        url = reverse('image-list')
        image_file = get_test_image()
        data = {"image": image_file}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_image_uuid(self):
        """Test that images get a unique uuid"""
        url = reverse('image-list')
        uuids = []
        for i in range(20):
            image_file = get_test_image()
            response = self.client.post(url, {"image": image_file})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            uuids.append(response.data['id'])
        self.assertEqual(len(set(uuids)), 20)

    def test_list_images(self):
        url = reverse('image-list')
        for i in range(20):
            image_file = get_test_image()
            self.client.post(url, {"image": image_file})
        response = self.client.get(url)
        self.assertEqual(len(response.data), 20)

    def test_get_image(self):
        """Create an image and get it's details"""
        image_file = get_test_image()
        response = self.client.post(
            reverse('image-list'), {"image": image_file})
        image_id = response.data['id']
        response = self.client.get(reverse('image-detail', args=(image_id,)))
        self.assertEqual(response.data['id'], image_id)

    def test_get_missing_image(self):
        """Test a missing image returns 404"""
        image_file = get_test_image()
        response = self.client.post(
            reverse('image-list'), {"image": image_file})
        response = self.client.get(reverse('image-detail', args=('bad',)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_rotate(self):
        """Test rotating an image 90 degrees clockwise"""
        image_file = get_test_image()
        response = self.client.post(
            reverse('image-list'), {"image": image_file})
        image_id = response.data['id']
        url = reverse('image-rotate', args=(image_id,))
        response = self.client.post(url, {'degrees': 90})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rotate_validation(self):
        """Test rotating an image by an invalid value"""
        image_file = get_test_image()
        response = self.client.post(
            reverse('image-list'), {"image": image_file})
        image_id = response.data['id']
        url = reverse('image-rotate', args=(image_id,))
        response = self.client.post(url, {'degrees': "ninety"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rotate_missing(self):
        """Test rotating an image that doesn't exist"""
        image_file = get_test_image()
        response = self.client.post(
            reverse('image-list'), {"image": image_file})
        url = reverse('image-rotate', args=('bad',))
        response = self.client.post(url, {'degrees': 90})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
