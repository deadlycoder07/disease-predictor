from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'role',
            'name',
            'registration_no',
            'email',
            'phone',
            'address',
            'address2',
            'city',
            'district',
            'state',
            'pincode'
        ]