from django.contrib import admin

# Register your models here.
from ibonchi.core.models.Profile import Profile
from ibonchi.core.models.MenuItem import MenuReviews, MenuItem, MenuRating, MenuImage
from ibonchi.core.models.Employee import Employee

admin.site.register(Profile)
admin.site.register(MenuItem)
admin.site.register(MenuReviews)
admin.site.register(MenuRating)
admin.site.register(MenuImage)
admin.site.register(Employee)