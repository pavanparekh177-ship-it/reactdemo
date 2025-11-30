from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50,default='abc')

    
    class meta:
        app_lable1='MYPRO'



