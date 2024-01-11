from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models import Portfolio
from ..serializers import PortfolioSerializer

# Create your views here.
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = PortfolioSerializer