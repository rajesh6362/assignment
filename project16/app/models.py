from django.db import models

# Create your models here.

class projectMainModel(models.Model):
    Title=models.CharField(max_length=20,)
    description=models.CharField(max_length=10)
    price=models.IntegerField(primary_key=True)
    uniquecode=models.CharField(max_length=20,unique=True)
    size=models.CharField(max_length=10)
    quality=models.CharField(max_length=10)


class productcolourmodel(models.Model):
    product=models.ForeignKey(projectMainModel,on_delete=models.CASCADE)
    colour=models.CharField(max_length=10)

class productimagemodel(models.Model):
    product=models.ForeignKey(projectMainModel,on_delete=models.CASCADE) 
    image=models.ImageField()  
