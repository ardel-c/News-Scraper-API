from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'