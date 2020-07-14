from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('form', views.FormPage, name='ResumeForm'),
    path('GeneratedResume', views.GeneratedResume, name='GeneratedResume')
]