from rest_framework import serializers

from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Products
        # fields = ['title', 'content', 'price', 'sale_price', 'nodiscount' ] 
        fields = ['title', 'content', 'price', 'sale_price', 'my_discount' ] 

    # def get_my_discount(self, obj):
    #     print("self", self)
    #     print("obj", obj)
    #     # print("obj.id", obj.id)
    #     try:
    #         return obj.nodiscount()
    #     except :
    #         return None
        
    def get_my_discount(self, obj):
        # print("self", self)
        # print("obj", obj)
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.nodiscount()
