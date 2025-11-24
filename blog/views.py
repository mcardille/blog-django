

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Post


def ListView(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/listadeposts.html', context)


def DetailView(request, pk):
    try:
        post = Post.objects.get(pk=pk) 
    except Post.DoesNotExist:
        raise Http404("Post não encontrado.") 

    context = {'post': post}
    return render(request, 'blog/detalhes.html', context)


def CreateView(request):
    if request.method == 'POST':
       
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, content=content)

        return redirect('blog:listadeposts') 

    return render(request, 'blog/criação.html')

def UpdateView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog:detalhes', pk=post.pk)

    context = {'post': post}
    return render(request, 'blog/atualização.html', context)


def DeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog:listadeposts')

    context = {'post': post}
    return render(request, 'blog/confirmaçãodel.html', context)