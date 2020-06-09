from django.contrib import admin

from .models import Diseases, symptoms, question,alert

# Register your models here.

admin.site.register(Diseases)
admin.site.register(symptoms)
admin.site.register(question)
admin.site.register(alert)