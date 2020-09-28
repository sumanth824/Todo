from django.db import models

# Create your models here.
class listapp(models.Model):
    content = models.CharField(max_length=40)
    Done = models.BooleanField(default=False)

    def __str__(self):
        return self.content