from django.urls import path
from . import views

app_name = 'blog' 
urlpatterns = [
    path('', views.ListView, name='listadeposts'), 
    path('new/', views.CreateView, name='criação'),
    path('<int:pk>/', views.DetailView, name='detalhes'),
    path('<int:pk>/edit/', views.UpdateView, name='atualização'),
    path('<int:pk>/delete/', views.DeleteView, name='delete'),
]