from django.db import models

# Create your models here.
class chat(models.Model):
    word=models.CharField(max_length=20)