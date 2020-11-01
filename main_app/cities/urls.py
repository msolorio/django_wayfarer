from django.urls import path
from . import views

# /cities/
urlpatterns = [
    path('', views.index, name='cities_index'),
    path('<int:city_id>/', views.detail, name='cities_detail')
]
