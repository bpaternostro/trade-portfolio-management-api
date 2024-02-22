from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models import Portfolio, PortfolioFinancialInstrument, PortfolioFinancialInstrumentOperation
from .. import serializers

# Create your views here.
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = serializers.PortfolioSerializer
    

class PortfolioFinancialInstrumentViewSet(viewsets.ModelViewSet):
    queryset = PortfolioFinancialInstrument.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = serializers.PortfolioUpdateDataSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.PortfolioUpdateDataSerializer
        if self.action == 'update-ticker':
            return serializers.PortfolioUpdateDataSerializer
        if self.action == 'create':
            return serializers.PortfolioCreateDataSerializer
        return serializers.PortfolioDataSerializer # I do 

    @action(detail=False, methods=['put'], url_path="update-ticker")
    def update_ticker(self, request):
        # Use a dictionary to quickly look up instances by ID
        instances_by_id = {instance.id: instance for instance in self.get_queryset()}
        updates = [
                    {"id": item["id"], "status": item["status"], "portfolio":item["portfolio"]}
                    for item in request.data
                ]
        # Perform bulk update
        for update in updates:
            instance = instances_by_id.get(update["id"])
            if instance:
                instance.status = update["status"]
                instance.save()

        portfolio = Portfolio.objects.get(id=updates[0]["portfolio"])
        return Response({"message": "Portfolio update successful", "portfolio_updated": serializers.PortfolioSerializer(portfolio).data})
    

    @action(detail=False, methods=['put'], url_path="move-ticker")
    def move_ticker(self, request):
        # Use a dictionary to quickly look up instances by ID
        instances_by_id = {instance.id: instance for instance in self.get_queryset()}
        updates = [
                    {"id": item["id"], "old_portfolio":item["old_portfolio"], "new_portfolio":item["portfolio"]}
                    for item in request.data
                ]
        # Perform bulk update
        for update in updates:
            instance = instances_by_id.get(update["id"])
            if instance:
                new_portfolio = Portfolio.objects.get(id=update["new_portfolio"])
                instance.portfolio = new_portfolio
                instance.save()

        portfolio = Portfolio.objects.get(id=updates[0]["old_portfolio"])
        return Response({"message": "Portfolio update successful", "portfolio_updated": serializers.PortfolioSerializer(portfolio).data})
    
    
    @action(detail=True, methods=['get'], url_path="get-sell")
    def get_sell(self, request, pk=None):
        queryset = PortfolioFinancialInstrument.objects.all()
        pfi = get_object_or_404(queryset, pk=pk)
        sells = PortfolioFinancialInstrumentOperation.objects.filter(portofolio_financial_instrument=pfi.id)
        if not sells:
            return Response({"message": "There is no sells"})
        return Response(serializers.PortfolioFinancialInstrumentOperationSerializer(sells, many=True).data)


class FinancialInstrumentViewSet(viewsets.ModelViewSet):
    queryset = PortfolioFinancialInstrument.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = serializers.PortfolioUpdateDataSerializer


class PortfolioFinancialInstrumentOperationViewSet(viewsets.ModelViewSet):
    queryset = PortfolioFinancialInstrumentOperation.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = serializers.PortfolioFinancialInstrumentOperationSerializer