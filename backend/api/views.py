from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
# Create your views here.

from products.serializers import ProductsSerializer
# def first_api(request, *args, **kwargs):
#     print(request.GET)
#     body = request.body
#     print("body: ", body)
#     data = {}
#     try:
#         data = json.loads(body)
#     except: 
#         pass 
#     data["params"] = dict(request.GET)
#     data["headers"] = dict(request.headers)
#     data["content_type"] = request.content_type
#     print(data)   
#     return JsonResponse(data)


# def first_api(request, *args, **kwargs):
#     data_model = Products.objects.all().order_by('?').first()  
#     print("data_model", data_model)  
#     # data = {}
#     # if data_model:
#     #     data['id'] = data_model.id
#     #     data['title'] = data_model.title
#     #     data['content'] = data_model.content
#     #     data['price'] = data_model.price
#     if data_model:
#        data = model_to_dict(data_model, fields=['id', 'title', 'price'])
#     json_to_str = json.dumps(data)
#     print("data", data)   
    
#     return JsonResponse(data)
#     # == 
#     # return HttpResponse(json_to_str, content_type='application/json')
#     # return HttpResponse(data)

# @api_view(['GET'])
# def first_api(request, *args, **kwargs):
#     data_model = Products.objects.all().order_by('?').first()  
#     if data_model:
#        data = model_to_dict(data_model, fields=['id', 'title', 'price', 'sale_price'])
#     print("data", data)   
    
#     return Response(data)  



# @api_view(['GET'])
# def first_api(request, *args, **kwargs):
#     instance = Products.objects.all().order_by('?').first()  
#     data = {}
#     if instance:
#        data = ProductsSerializer(instance).data
#     print("data", data)   
    
#     return Response(data)  
    


# @api_view(['POST'])
# def first_api(request, *args, **kwargs):
#    serializer = ProductsSerializer(data=request.data)
#    if serializer.is_valid(raise_exception=True):
#       # data = serializer.data
#       # instance = serializer.save() # the way to create the instance
#       # print("data", instance)
#       return Response(serializer.data) 
#    # return Response({"message": "Invalid data"})   

@api_view(['POST'])
def first_api(request, *args, **kwargs):
   serializer = ProductsSerializer(data=request.data)
   if serializer.is_valid(raise_exception=True):
      # data = serializer.data
      # instance = serializer.save() # the way to create the instance
      # print("data", instance)
      return Response(serializer.data) 
   # return Response({"message": "Invalid data"})   
    