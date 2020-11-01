from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.detail, name='posts_detail')
]