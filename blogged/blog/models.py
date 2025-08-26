from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  
    content = models.TextField(default="(no content)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering =('-created_at',)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering =('-created_at',)
        

    def __str__(self):
        return f'{self.name} - {self.post.title}'    
# Create your models here. 
