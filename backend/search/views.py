from rest_framework import generics
from products.serializers import ProductsSerializer
from products.models import Products
from . import client
from rest_framework.response import Response

class SearchAlgolia(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        public = str(request.GET.get('public')) != "0"
        query = request.GET.get('q')
        tags = request.GET.get('tags') or []
        print(user, public, query, tags)
        if not query:
            return Response('', status=400)
        
        results = client.perform_search(query, tags=tags, user=user, public=public)  
        return Response(results)
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