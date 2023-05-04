from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('stationary', 'stationary'),
    ('Electronic', 'Electronic'),
    ('Food', 'Food')
)
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'
    
    def __str__(self):
        return f'{self.name}--{self.category}--{self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    date_odered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product}--{self.quantity}'

