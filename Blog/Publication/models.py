from django.db import models
#from Author.models import Author

class Publication(models.Model):
    #Author = models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name="Nome do Autor")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    date_publication = models.DateField()
    pub_text = models.TextField()
class Meta:
    db_table = 'publications'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title