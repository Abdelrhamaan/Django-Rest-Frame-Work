from rest_framework import generics
from products.serializers import ProductsSerializer
from products.models import Products

class SearchList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Products.objects.none() 
        if q is not None:
            user  = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results