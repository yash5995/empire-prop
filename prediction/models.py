from django.db import models
class Register(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)

# Create your models here.
