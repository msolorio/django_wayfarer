from django.urls import path, include
from ..views import home


urlpatterns = [
    # Auth
    path('accounts/signup', home.signup, name='signup'),
    # Intro
    path('', home.index, name='index'),
    path('about/', home.about, name='about'),
    # App
    path('cities/', include('main_app.urls.cities')),
    path('profiles/', include('main_app.urls.profiles')),
    path('posts/', include('main_app.urls.posts')),
]
