from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import ImageViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register('images', ImageViewSet)

urlpatterns += router.urls
