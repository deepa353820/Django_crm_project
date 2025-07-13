from django.db import models

# Create your models here.

class tests(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    emp_id = models.IntegerField()
    Class = models.CharField(max_length=50)

def __str__(self):
    return tests.name