from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/templates/media/')

    def __str__(self):
        return self.name