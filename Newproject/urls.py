from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('about', views.AboutPage, name='AboutPage'),
    path('contact', views.ContactPage, name='ContactPage'),
    path('form', views.FormPage, name='ResumeForm'),
    path('GeneratedResume', views.GeneratedResume, name='GeneratedResume')
]

urlpatterns += staticfiles_urlpatterns() # It will work only in debug mode not in production mode