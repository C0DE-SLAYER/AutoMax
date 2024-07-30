from django import forms
from django.contrib.auth.models import User

from .models import Location, Profile
from .widget import CustomImageFieldWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = {
            'address_1', 'address_2', 'city', 'state', 'zip_code'
        }