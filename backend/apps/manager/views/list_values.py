from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from ..constants import *

class ListValuesViewSet(viewsets.ModelViewSet):

    def list(self, request):
        return Response({
            "portfolio_types":PortfolioType.choices,
            "status": Status.choices
        })
