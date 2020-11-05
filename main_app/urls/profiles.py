from django.urls import path, include
from ..views import profiles as profiles_views

urlpatterns = [
    path('', profiles_views.detail, name='profiles_detail'),
    path('update_profile_city/', profiles_views.update_profile_city, name='update_profile_city'),
]
