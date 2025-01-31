from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_experience, name='record_experience'),
]