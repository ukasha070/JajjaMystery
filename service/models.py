from django.db import models

import os
import uuid

def handle_service_image(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return f"services/image_{instance.id}{file_extension}"


# Create your models here.
class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, blank=False,
                          null=False, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=handle_service_image)
    published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class ServiceList(models.Model):
    id = models.UUIDField(default=uuid.uuid4, blank=False,
                          null=False, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title