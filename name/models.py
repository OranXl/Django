from django.db import models

class Category(models.Model):
    """Категория новостей"""
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Post(models.Model):
    """Для новостных постов"""
    title = models.CharField(max_length=255)
    content = models.TextField(default='Статья')
    craete_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    wathed = models.IntegerField(default=0)
    is_publeshed = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)