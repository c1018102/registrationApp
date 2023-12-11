from django.urls import path
from . import views

app_name = 'moduleregistrationsystem'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('modules', views.modules, name='modules')
]