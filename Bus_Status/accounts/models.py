from django.db import models

# Create your models here.

# from django.contrib.auth.models import User


class UserRegistration(models.Model):
    id_here = models.CharField( max_length=100)
    username = models.CharField( max_length=100)
    email = models.EmailField( max_length=35)
    password1 = models.CharField( max_length=50)
    password2 = models.CharField(max_length=50)



