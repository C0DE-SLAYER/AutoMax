from django.db import models
import uuid

from users.models import Profile, Location
from .const import CARS_BRANDS, TRANSMISSION_OPTIONS
from .util import user_listing_dir

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=25, default=None, choices=CARS_BRANDS)
    model = models.CharField(max_length=64)
    vin = models.CharField(max_length=17, unique=True)
    mileage = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=25)
    description = models.TextField()
    engine = models.CharField(max_length=25)
    transmission = models.CharField(max_length=25, default=None, choices=TRANSMISSION_OPTIONS)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_dir)

    def __str__(self):
        return f"{self.seller.user.username}'s Listing: {self.model}"
    
class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.model} listing liked by {self.profile.user.username}'