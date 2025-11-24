

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Post
from .forms import Forms

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
        form = Forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('blog:listadeposts') 
    else:
        form = Forms()

    return render(request, 'blog/criação.html', {'form': form})

def UpdateView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = Forms(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detalhes', pk=post.pk)
    else:
        form = Forms(instance=post)
    return render(request, 'blog/atualização.html', {'form': form})


def DeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog:listadeposts')

    context = {'post': post}
    return render(request, 'blog/confirmaçãodel.html', context)