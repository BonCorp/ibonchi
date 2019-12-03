from django.contrib import admin

# Register your models here.
from ibonchi.core.models.Profile import Profile
from ibonchi.core.models.MenuItem import MenuReviews, MenuItem, MenuRating, MenuImage

admin.site.register(Profile)
admin.site.register(MenuItem)
admin.site.register(MenuReviews)
admin.site.register(MenuRating)
admin.site.register(MenuImage)