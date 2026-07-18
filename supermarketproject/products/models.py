from django.db import models


class products(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
# Create your models here.
