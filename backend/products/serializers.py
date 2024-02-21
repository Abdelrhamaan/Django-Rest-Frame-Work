from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Products
from .validators import validate_title, validate_price, unique_product_validator

class ProductsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product_detail',
        lookup_field = 'pk'
    )
    email = serializers.EmailField(write_only = True)
    title = serializers.CharField(validators=[validate_title, 
                                              unique_product_validator]) # second way  to make custom validation
    # price = serializers.DecimalField(max_digits=4, decimal_places=2,validators=[validate_price])
    class Meta:
        model = Products
        # fields = ['title', 'content', 'price', 'sale_price', 'nodiscount' ] 
        fields = [
            # 'user',
            'url', 
            'edit_url',
            'email',
            'pk', 
            'title', 
            'content', 
            'price', 
            'sale_price', 
            'my_discount' ] 
    
    # def validate_title(self, value): # firstway to make custom validation  
    #     # qs = Products.objects.filter(title__exact=value)
    #     qs = Products.objects.filter(title__iexact=value)# to make it case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"this {value} is already exists")
    #     return value

    def validate_price(self, value):
        price = value
        if price > 60:
            raise serializers.ValidationError(f"{value} shouldn't be more than 60")
        return value     



    # def create(self, validated_data):
    #     email = validated_data.pop('email') # we can do the same thing in preform_create in view cbv
    #     # send email here and not save it to the database
    #     obj = super().create(validated_data)
    #     return obj

    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product_edit', kwargs={'pk': obj.pk}, request=request)
        
    
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
