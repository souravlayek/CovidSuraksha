from django.urls import path
from . import views

urlpatterns = [
    path('communityhome/', views.PostView, name = 'communityhome'),
    path('newpost/',views.PostCreate, name='newpost'),
    path('addpost/',views.AddPost, name='addpost'),
    path('like/<int:id>', views.like_post, name = 'like'),
    path('dislike/<int:id>', views.dislike_post, name = 'dislike'),
    path('comment/<int:id>', views.CommentPost, name = 'comment'),
    path('search', views.search, name = 'search'),
    path('filter/<str:filter_by>', views.filterpost, name = 'filter'),
    path('sort/<str:sort_by>', views.sortpost, name = 'sort')
]
