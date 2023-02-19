from django.db import models
from cloudinary.models import CloudinaryField


class NGO(models.Model):
    """Data base of NGO's"""
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    logo = CloudinaryField('image', default='placeholder')
    website_url = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    areas_of_focus = models.ManyToManyField('FocusArea', blank=True)

    def __str__(self):
        return self.name


class FocusArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
