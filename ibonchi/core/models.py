from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=64)
    street_address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    cuisine = models.CharField(max_length=64)
    tagline = models.TextField()
    open_hours = models.TimeField()
    close_hours = models.TimeField()

    def __str__(self):
        return f"{self.id} \n Name: {self.name}\n {self.tagline} \n Address: {self.street_address} {self.city}, {self.state} {self.zipcode} " \
               f"\n Phone: {self.phone} \n Cuisine: {self.cuisine} \n Open: {self.open_hours} - Close: {self.close_hours}"
