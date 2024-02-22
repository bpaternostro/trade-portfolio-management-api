from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from ..models import Trader, Portfolio
from ..serializers import TraderSerializer, CreatePortfolioSerializer, PortfolioSerializer


class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = TraderSerializer

    @action(detail=True, methods=['post'], url_path="create-portfolio")
    def create_portfolio(self, request, pk=None):
        trader = self.get_object()
        serializer = CreatePortfolioSerializer(data=request.data)
        if serializer.is_valid():
            new_portfolio = Portfolio(**serializer.validated_data)
            new_portfolio.save()
            trader.portfolios.add(new_portfolio.id)
            trader.save()
            return Response({'status': 'portfolio created succesfully', "new_portfolio_id":new_portfolio.id, "portfolios":PortfolioSerializer(trader.portfolios, many=True).data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        