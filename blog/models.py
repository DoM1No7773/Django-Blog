from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    created_at = models.DateTimeField('date published')
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField('date published',default=None)

    def __str__(self):
        return self.content