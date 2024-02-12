from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99)

    @property
    def sale_price(self):
        return float(self.price) * 0.8
    
    def nodiscount(self):
        return "no discount for this transaction"