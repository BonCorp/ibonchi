from django import forms
from django.views.generic import UpdateView

from .models import Profile

from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'street_address', 'city', 'state', 'zipcode', 'phone',
                  'cuisine', 'tagline', 'open_hours', 'close_hours']


