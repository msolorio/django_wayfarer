from django.urls import path, include
from ..views import profiles as profiles_views

urlpatterns = [
    path('', profiles_views.detail, name='profiles_detail')
]
