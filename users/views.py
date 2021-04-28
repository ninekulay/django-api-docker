from django.shortcuts import render
from .models import Leave,UserLeave,GetLeave
from rest_framework import viewsets
from .serializers import LeaveSerializer,UserLeaveSerializer,GetLeaveSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class GetLeaveViewSet(viewsets.ModelViewSet):
    queryset = GetLeave.objects.all()
    serializer_class = GetLeaveSerializer

class UserLeaveViewSet(viewsets.ModelViewSet):
    queryset = UserLeave.objects.all()
    serializer_class = UserLeaveSerializer


