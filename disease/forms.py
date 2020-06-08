from django import forms
from .models import Diseases, symptoms, question, answer


# create forms


class Diseaseform(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = "__all__"
        exclude=['Expected_recovery_date']

class Symptomform(forms.ModelForm):
    class Meta:
        model = symptoms
        fields = "__all__"

class QuestionForm(forms.ModelForm):
    class Meta:
        model = answer
        fields = "__all__"