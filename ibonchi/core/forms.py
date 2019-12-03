from django import forms
from django.forms import FileField

from ibonchi.core.models import MenuItem, MenuImage
from ibonchi.core.models.Profile import Profile
from ibonchi.core.models import Employee


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'street_address', 'city', 'state', 'zipcode', 'phone',
                  'cuisine', 'tagline', 'open_hours', 'close_hours']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'price', 'calories', 'category']


class MenuImageForm(forms.ModelForm):
    class Meta:
        model = MenuImage
        fields = ['image']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'photo']
