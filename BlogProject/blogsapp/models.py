from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    descript = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
