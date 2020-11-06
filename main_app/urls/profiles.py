from django.urls import path, include
from ..views import profiles as profiles_views

urlpatterns = [
    path('<int:profile_id>/', profiles_views.detail, name='profiles_detail'),
    path('profiles_edit/', profiles_views.edit, name='profiles_edit'),
    path('profiles_update/', profiles_views.update, name='profiles_update'),
    path('profiles_update_city/', profiles_views.profiles_update_city, name='profiles_update_city'),
]
