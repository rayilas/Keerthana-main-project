from django.db import models

# Create your models here.
class Datas(models.Model):
    First_Name=models.CharField(max_length=20,default="")
    Last_Name=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=50,default="")
    Password=models.CharField(max_length=30,default="")
    Conform_Password=models.CharField(max_length=30,default="")
    

