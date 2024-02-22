from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.manager.urls import router as manager_router
#from apps.core.urls import urlpatterns as core_urls

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.registry.extend(manager_router.registry)

app_name = "api"
urlpatterns = router.urls # + core_urls
