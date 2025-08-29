from rest_framework import routers
from .views import PlanetViewSet

# Using default router
router = routers.DefaultRouter()
# Use the same api with different methods POST, GET etc.
router.register(r'planets', PlanetViewSet)

urlpatterns = router.urls