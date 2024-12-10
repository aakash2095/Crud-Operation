from django.db import models

# Create your models here.

class Crud(models.Model):
    name=models.CharField(max_length=60)
    Email=models.EmailField(max_length=70)