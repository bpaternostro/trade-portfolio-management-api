from rest_framework.routers import DefaultRouter
from .views.portfolio import *

router = DefaultRouter()
router.register(r"portfolio", PortfolioViewSet)