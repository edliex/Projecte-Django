from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name="posts-page"),
    path('posts/<slug:slug>/', views.post_detail, name="post-detail"),
    path('autors/', views.authors_list, name="autors-page"),
    path('autors/<int:id>/', views.author_detail, name='author-detail'),
    path('tags/', views.tag_list, name="tags-page"),
    path('tags/<int:id>/', views.tag_detail, name="tag-detail"),
    ]