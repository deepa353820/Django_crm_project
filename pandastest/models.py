from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50,null=True)
    emp_id = models.IntegerField()
    rank = models.IntegerField()

def __str__(self):
    return self.name

class test(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    emp_id = models.IntegerField()
    Class = models.CharField(max_length=50)
