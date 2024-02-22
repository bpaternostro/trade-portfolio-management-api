from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models import FinancialInstrument
from ..serializers import FinancialInstrumentSerializer


class FinancialInstrumentViewSet(viewsets.ModelViewSet):
    queryset = FinancialInstrument.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = FinancialInstrumentSerializer