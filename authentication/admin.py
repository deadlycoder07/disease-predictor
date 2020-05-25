from django.contrib import admin
from .models import CustomUser,Hospital, Clinic

admin.site.register(Hospital)
admin.site.register(CustomUser)
admin.site.register(Clinic)
# Register your models here.
