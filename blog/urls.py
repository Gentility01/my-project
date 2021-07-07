from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, like_unlike_post
import blog


# app_name = 'blog'

urlpatterns = [
    path('',PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>',UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),

    path('liked/', like_unlike_post, name='like-post-view' ),

    path('gallery/new/', views.gallery, name = 'gallery'),
    path('photos/<str:pk>/', views.viewPhotos, name = 'photo'),
    path('addPhoto/', views.addPhoto, name = 'add')
]
