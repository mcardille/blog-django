from django.urls import path
from . import views

app_name = 'blog' 
urlpatterns = [
    path('', views.PostListView.as_view(), name='listadeposts'), 
    path('new/', views.PostCreateView.as_view(), name='criação'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detalhes'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='atualização'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_pk>/comment/new/', views.CommentCreateView, name='comment_create'),
]