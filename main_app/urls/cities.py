from django.urls import path
from ..views import cities as cities_views

# /cities/
urlpatterns = [
    path('', cities_views.index, name='cities_index'),
    path('<int:city_id>/', cities_views.detail, name='cities_detail')
]
