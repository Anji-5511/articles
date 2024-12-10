from django.db import models

# Create your models here.

class article(models.Model):
    h3=models.CharField(max_length=1000)
    p=models.CharField(max_length=1000)
    header=models.CharField(max_length=1000)
    content=models.CharField(max_length=1000)
