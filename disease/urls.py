from django.urls import path

from . import views

app_name = 'disease'

urlpatterns = [
    path('diseaseform/', views.diseaseview, name = "diseaseform"),
    path('thanks/', views.thanks, name="thanks"),
    path('checkdisease/', views.usercheckview, name="usercheckview"),
    path('analysis/', views.analysis, name="analysis"),
    path('',views.home,name='index'),
    path('contact/', views.contact, name="contact"),
    path('about/', views.aboutus, name="aboutus"),
    path('privacy/', views.privacy, name="privacy"),
    
    
    
]