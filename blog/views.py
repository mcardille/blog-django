

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/listadeposts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detalhes.html'
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset=queryset)
        except Http404:
            raise Http404

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/criação.html'
    fields = ['title', 'content']
    def get_success_url(self):
        return reverse_lazy('blog:detalhes', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/atualização.html'
    fields = ['title', 'content']
    def get_success_url(self):
        return reverse_lazy('blog:detalhes', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/confirmaçãodel.html'
    success_url = reverse_lazy('blog:listadeposts')