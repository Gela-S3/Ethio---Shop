from rest_framework.routers import DefaultRouter
from .views import ProductViewSet  # or whatever ViewSet you have

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
