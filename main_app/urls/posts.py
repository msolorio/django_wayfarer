from django.urls import path
from ..views import posts as posts_views

urlpatterns = [
    path('<int:post_id>/', posts_views.detail, name='posts_detail'),
    path('create_post/city/<int:city_id>/', posts_views.create_post, name='create_post'),
    path('add_post/city/<int:city_id>/', posts_views.add_post, name='add_post'),
]
