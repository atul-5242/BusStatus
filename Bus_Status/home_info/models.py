from django.db import models

# Create your models here.
class search(models.Model):
    Location = models.CharField( max_length=100)
    Time= models.CharField( max_length=100)
