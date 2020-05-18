from django import forms
from .models import Diseases


# create forms


class Diseaseform(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = "__all__"
        exclude=['Expected_recovery_date']
