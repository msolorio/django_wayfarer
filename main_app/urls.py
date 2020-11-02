from django.urls import path, include
from . import views


urlpatterns = [
    # Auth
    path('accounts/signup', views.signup, name='signup'),
    # Intro
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # App
    path('cities/', include('main_app.cities.urls')),
    path('profiles/', include('main_app.profiles.urls')),
    path('posts/', include('main_app.posts.urls')),
]
