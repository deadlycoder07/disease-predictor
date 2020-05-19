from django.contrib import admin

from .models import Diseases, symptoms

# Register your models here.

admin.site.register(Diseases)
admin.site.register(symptoms)