from django.db import models

# Create your models here.


class customers(models.Model):
    name = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name