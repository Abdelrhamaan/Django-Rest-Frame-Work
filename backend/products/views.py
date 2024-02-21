from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Products
from .serializers import ProductsSerializer
from  rest_framework.response import Response
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from api.permissions import IsEditorStaffPermission
from api.mixins import StaffEditorMixinPermissions

# Create your views here.


# def first_api(request, *args, **kwargs):
#     data_model = Products.objects.all().order_by('').first()    
#     data = {}
#     if data_model:
#         data['title'] = data_model.title
#         data['content'] = data_model.content
#         data['price'] = data_model.price
    
#     return JsonResponse(data)



# class ProductCreateView(generics.CreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         if not content:
#             content = title
#         serializer.save(content=content)
# product_create_view = ProductCreateView.as_view()

# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     authentication_classes = [authentication.SessionAuthentication,
#                               authentication.TokenAuthentication] 
#     # permission_classes = [permissions.IsAuthenticated] # ---> 
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # ---> you can get put you cannot post
#     # permission_classes = [IsEditorStaffPermission] # ---> make custom permissions
#     permission_classes = [permissions.IsAdminUser, IsEditorStaffPermission] # ---> make custom permissions
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         if not content:
#             content = title
#         serializer.save(content=content)
# product_list_create_view = ProductListCreateView.as_view()


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if not content:
            content = title
        serializer.save(content=content)

product_mixins_view = ProductMixinView.as_view()

class ProfuctDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


product_detail_view = ProfuctDetailView.as_view()

@api_view(["GET", "POST"])
def list_Create(request, pk=None, *arg, **kwargs):
    
    if request.method == 'GET':
        if pk is not None:
            # obj = Products.objects.filter(pk=pk)
            obj = get_object_or_404(Products, pk=pk)
            serialzier = ProductsSerializer(obj, many=False)
            return Response(serialzier.data)

        qs = Products.objects.all()
        serialzier = ProductsSerializer(qs, many=True)
        return Response(serialzier.data)
    if request.method == 'POST':
        serialzier = ProductsSerializer(data=request.data)
        if serialzier.is_valid():
            title = serialzier.validated_data.get('title')
            content = serialzier.validated_data.get('content')
            if not content:
                content = title
            serialzier.save(content=content)
            return Response(serialzier.data)
        return Response({"message": "Invalid data"})
    



class ProfuctUpdateView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def preform_update(self, serialzier):
        instance = serialzier.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProfuctUpdateView.as_view()




class ProductDestroyView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def preform_destroy(self, instance):
        super().preform_destroy(instance)

product_destroy_view = ProductDestroyView.as_view()



# ====================================================

"""
make mixin peermession class to inherit from it in all classes 
instead of write this line     
permission_classes = [permissions.IsAdminUser, IsEditorStaffPermission]
in every class based view 
"""

class ProductListCreateView(
            StaffEditorMixinPermissions,
            generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer)
        print(serializer.validated_data)
        # this way better than overriding create and update methods in serializer it self
        email = serializer.validated_data.pop('email', None)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if not content:
            content = title
        serializer.save(user=self.request.user, content=content)


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Products.objects.none()
        return qs.filter(user=user)

            
product_list_create_view = ProductListCreateView.as_view()


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer