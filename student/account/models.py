from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=10)
class Course(models.Model):
    name=models.CharField(max_length=10)
    description=models.CharField(max_length=50)
    semester=models.IntegerField()
    fee=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Coursedeatils(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=400)
    def __str__(self):
       return self.name
   
class Staff(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)  
    password=models.CharField(max_length=15)  
    phno=models.CharField(max_length=12)  
     
    def __str__(self):
        return self.name
    
    