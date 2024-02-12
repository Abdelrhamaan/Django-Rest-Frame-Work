from django.urls import path
from .views import ProfuctDetailView, product_detail_view, product_list_create_view, list_Create, product_update_view,\
      product_destroy_view,  product_mixins_view

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    # '<int:pk>', ProfuctDetailView.as_view(),
    # path('<int:pk>/', product_detail_view,),
    path('<int:pk>/update/', product_update_view,),
    path('<int:pk>/delete/', product_destroy_view,),
    # path('', product_mixins_view,), # list all products
    # path('<int:pk>/', product_mixins_view,), # get one product
    # path('', product_mixins_view), # create new product
    path('', product_list_create_view),
    # path('<int:pk>/', list_Create,),
    # path('', list_Create),
]
