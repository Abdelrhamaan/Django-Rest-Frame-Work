from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Products

@register(Products) # == admin.site.register(Products, ProductsAdmin)  
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public',
    ]
    tags = 'get_random_tag'