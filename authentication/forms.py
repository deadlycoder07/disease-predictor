from django import forms
from .models import CustomUser, Clinic, Hospital
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = [
            'phone',
            'email',
            'password',
        ]

class ClinicInfoForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = "__all__"

class HospitalInfoForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = "__all__"
        exclude = ['user']