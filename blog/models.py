from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    created_at = models.DateTimeField('date published')
    #TODO: created_by ,but now i dont know how to do that 

    def __str__(self):
        return self.title
