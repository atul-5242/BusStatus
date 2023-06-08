from django.db import models

# Create your models here.

class Bus_infor(models.Model):
    Location = models.CharField( max_length=100)
    Time= models.CharField( max_length=100)
    Bus_no= models.EmailField( max_length=35)
    

