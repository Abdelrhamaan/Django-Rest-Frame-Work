from products.viewsets import ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products-abc', ProductsViewSet, basename='products')
urlpatterns = router.urls
print("router.urls", router.urls)
