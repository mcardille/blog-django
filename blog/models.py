
from django.db import models
from django.contrib.auth import get_user_model 


User = get_user_model() 




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    description = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    logo = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(Category, related_name='posts', verbose_name="Categorias")
    def __str__(self):
        return self.title

class Comment(models.Model):   
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Comentário")
    data = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'Comentário de {self.autor} em {self.post.title}'

    class Meta:
        ordering = ['data']
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"