from django.urls import path
from . import views

app_name = 'moduleregistrationsystem'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('modules', views.modules, name='modules'),
    path('add_module', views.add_module, name='add_module'),
    path('edit_module', views.edit_module, name='edit_module'),
    path('delete_module', views.delete_module, name='delete_module'),
]

