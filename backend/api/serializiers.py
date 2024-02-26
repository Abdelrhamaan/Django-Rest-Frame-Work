from rest_framework import serializers

# nested serializers  
class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product_detail',
        lookup_field = 'pk'
    )
    title = serializers.CharField(read_only=True)


class UserProductSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)


    def get_other_products(self, obj):
        print(obj)
        user = obj
        my_products = user.products_set.all()[:5]
        print(my_products)
        return UserProductInlineSerializer(my_products, many=True, context=self.context).data