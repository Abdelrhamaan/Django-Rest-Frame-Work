from .serializers import ProductsSerializer
from rest_framework import viewsets, mixins
from .models import Products

class ProductsViewSet(viewsets.ModelViewSet):  
    """
    gives you url for 
    get - post - put - patch - delete methods
    but if you don't want all crud operations
    you can use generic viewsets with mixins as below.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer



class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet,
        ):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'


product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})