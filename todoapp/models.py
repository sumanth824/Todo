from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class listapp(models.Model):
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    content = models.CharField(max_length=40)
    Done = models.BooleanField(default=False)

    def __str__(self):
        return self.content
