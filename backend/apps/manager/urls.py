from rest_framework.routers import DefaultRouter
from .views.portfolio import *
from .views.financial_instrument import *
from .views.trader import *
from .views.list_values import *

router = DefaultRouter()
router.register(r"financial-instrument", FinancialInstrumentViewSet)
router.register(r"portfolio", PortfolioViewSet)
router.register(r"portfolio-financial-instrument", PortfolioFinancialInstrumentViewSet)
router.register(r"portfolio-financial-instrument-op", PortfolioFinancialInstrumentOperationViewSet)
router.register(r"list-values", ListValuesViewSet, basename="list_values")
router.register(r"", TraderViewSet)