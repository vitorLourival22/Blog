from django.db import models
from Author.models import Author
from django.contrib.auth.models import User

class Publication(models.Model):
    Author = models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name="Nome do Autor")
    date_publication = models.DateTimeField()
    pub_text = models.CharField(max_length=100,verbose_name="Texto da Publicação")
    title = models.CharField(max_length=100,verbose_name="itulo da Publicação")
class Meta:
    db_table = 'publications'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)  # Texto da postagem
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Imagem opcional
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.text[:50]  # Retorna os primeiros 50 caracteres do texto