from django.db import models
from cloudinary.models import CloudinaryField


class NGO(models.Model):
    """Data base of NGO's"""
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    logo = CloudinaryField('image', default='placeholder')
    website_url = models.URLField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=False, blank=False)
    areas_of_focus = models.ManyToManyField('FocusArea', blank=True)

    def __str__(self):
        return self.name


class FocusArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
