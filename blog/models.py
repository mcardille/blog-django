from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() 
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#class Post(models.Model):
    #title = models.CharField(max_length=200, verbose_name="Título")
    #content = models.TextField(verbose_name="Conteúdo HTML")
    #date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Data de Postagem")

    #class Meta:
       
        #ordering = ['-date_posted']
        #verbose_name = "Postagem"
        #verbose_name_plural = "Postagens"