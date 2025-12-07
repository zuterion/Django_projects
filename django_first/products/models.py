from django.db import models

# Create your models here.

class ProductLine(models.Model):
    productLine = models.CharField(primary_key=True, max_length=50)
    textDescription = models.CharField(max_length=4000, null=True, blank=True)
    htmlDescription = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'productlines'

    def __str__(self):
        return self.productLine
