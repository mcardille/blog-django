

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from .models import Post, Comment, Category
from .forms import Forms, CommentForm
from django.contrib.auth.decorators import login_required
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

@login_required 
def CommentCreateView(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = post
            comment.autor = request.user 
            comment.save() 

         
            return redirect('blog:detalhes', pk=post.pk)

    
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/comment_create.html', context)

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset=queryset)
        except Http404:
            raise Http404("Essa categoria não existe.")