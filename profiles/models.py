from django.db import models
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User


class Profile(models.Model):
    """User Profile Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    county = models.CharField(
        max_length=80, null=True, blank=True)
    postcode = models.CharField(
        max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label='Country', null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, created, instance, **kwargs):
    """
    Create or Update Profile Models on User save
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
