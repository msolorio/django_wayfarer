from django.urls import path
from ..views import posts as posts_views

urlpatterns = [
    path('<int:post_id>/', posts_views.detail, name='posts_detail')
]
