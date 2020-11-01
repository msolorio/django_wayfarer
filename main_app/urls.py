from django.urls import path, include
from . import views


urlpatterns = [
    path('cities/', include('main_app.cities.urls')),
    path('profiles/', include('main_app.profiles.urls')),
    path('posts/', include('main_app.posts.urls')),
    path('', views.index, name='index'),
]
