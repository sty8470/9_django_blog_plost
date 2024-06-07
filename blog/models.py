from django.db import models

# Create your models here.
class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_post'