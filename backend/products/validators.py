from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Products


def validate_title(value):   
        # qs = Products.objects.filter(title__exact=value)
        qs = Products.objects.filter(title__iexact=value)# to make it case insensitive
        if qs.exists():
            raise serializers.ValidationError(f"this {value} is already exists")
        return value

unique_product_validator = UniqueValidator(queryset=Products.objects.all(), lookup='iexact')    

def validate_price(value):
    price = value
    if price > 60:
        raise serializers.ValidationError(f"{value} shouldn't be more than 60")
    return value 