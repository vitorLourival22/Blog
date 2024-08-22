from django.db import models
from Author.models import Author

class Publication(models.Model):
    Author = models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name="Nome do Autor")
    date_publication = models.DateTimeField()
    pub_text = models.CharField(max_length=100,verbose_name="Texto da Publicação")
    title = models.CharField(max_length=100,verbose_name="itulo da Publicação")
    pub_image = models.ImageField(
        upload_to='publications_images/',
    )
class Meta:
    db_table = 'publications'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title