import uuid
from django.db import models


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
