from . import views
from django.urls import path
from .views import AnotherPostDetail


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('another_post/<slug>/', AnotherPostDetail.as_view(), name='another_post_detail'),
]