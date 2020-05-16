from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers, viewsets
from . import views
router= routers.DefaultRouter()

urlpatterns= [
    path('', include(router.urls)),
    path('rest/signup',views.UserRegistrationView.as_view(),name='registerview'),
    path('rest/signup/hospital',views.HospitalRegistration.as_view(),name='hostpitalregister'),
    path('rest/signup/clinic',views.ClinicRegistration.as_view(),name='clinc registration'),
    path('rest/login',views.UserLoginView.as_view(),name='login view'),
]