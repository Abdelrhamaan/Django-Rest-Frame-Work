from django.urls import path
from .views import SearchList, SearchAlgolia

urlpatterns = [
    path('', SearchAlgolia.as_view(), name='search'),
    # path('', SearchList.as_view(), name='search'),
]
