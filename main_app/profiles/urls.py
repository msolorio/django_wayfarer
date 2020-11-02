from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.detail, name='profiles_detail')
]
