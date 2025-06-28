from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User 
# 
class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='pages_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
#
    def __str__(self):
        return self.title
#
class Comment(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("Comentario")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.author.username} en "{self.page.title}"'