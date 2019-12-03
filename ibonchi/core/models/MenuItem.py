from django.db import models
from django.contrib.auth.models import User


# create Menu Item Model
class MenuItem(models.Model):
    Appetizers = 'Appetizers'
    Entree = 'Entree'
    Dessert = 'Dessert'
    DrinksNA = 'Drinks - Non Alcoholic'
    DrinksA = 'Drinks - Alcoholic'

    category_choices = [
        (Appetizers, 'Appetizers'),
        (Entree, 'Entree'),
        (Dessert, 'Dessert'),
        (DrinksNA, 'Drinks - Non Alcoholic'),
        (DrinksA, 'Drinks - Alcoholic'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField(default=0)
    category = models.CharField(choices=category_choices, max_length=21, default=Appetizers)

    def __str__(self):
        return f"{self.user}'s menu item: {self.title} - {self.description} - {self.price}"


class MenuImage(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images')

    def __str__(self):
        return f"{self.menu_item.title}'s image: {self.image}"


class MenuReviews(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=None, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"For menu item: {self.menu_item.title}\n {self.user.username} says: {self.text}"


class MenuRating(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=None, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"For the menu item: {self.menu_item.title}\n {self.user.username} gave a rating of {self.rating}"

# Add Model For Table
# user (Many To Many), menu item, capacity
