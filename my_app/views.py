from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Position, Employee
from .serializers import PositionSerializer, EmployeeSerializer


class PositionListCreate(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer









