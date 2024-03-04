from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import random
# Create your models here.



TAG_MODEL_VALUES = ['cars', 'electronics', 'fruits', 'food']
class ProductQuerySet(models.QuerySet):
    def is_puplic(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)  
        qs = self.is_puplic().filter(lookup)
        if user is not None:
            qs2= qs.filter(user=user)
        qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> models.QuerySet:
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().is_public().search(query, user=user)

class Products(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) 
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    def is_public(self):
        return self.public

    @property
    def sale_price(self):
        return float(self.price) * 0.8
    
    def get_tags_list(self):
        return [random.choice(TAG_MODEL_VALUES)]
    
    
    def nodiscount(self):
        return "no discount for this transaction"