from django.urls import path,re_path

from . import views

app_name = 'disease'

urlpatterns = [
    path('diseaseform/', views.diseaseview, name = "diseaseform"),
    path('thanks/', views.thanks, name="thanks"),
    path('checkdisease/', views.usercheckview, name="usercheckview"),
    path('checkbyquestion/', views.userquestion, name="userquestion"),
    path('analysis2/', views.qanalysis, name="analysis2"),
    path('analysis/', views.analysis, name="analysis"),
    path('',views.index,name='index'),
    path('HospitalDashboard/', views.Hhome, name='HospitalDashboard'),
    path('contact/', views.contact, name="contact"),
    path('about/', views.aboutus, name="aboutus"),
    path('privacy/', views.privacy, name="privacy"),
    re_path(r'^.*\.html', views.pages, name='pages'),
    
    
]