from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('thank-you/', views.thank_you, name='thank_you'),
]