from django.urls import path
from .views import SearchList

urlpatterns = [
    path('', SearchList.as_view(), name='search'),
]
