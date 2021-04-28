from django.shortcuts import render
from .models import Leave,UserLeave
from rest_framework import viewsets
from .serializers import LeaveSerializer,UserLeaveSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class UserLeaveViewSet(viewsets.ModelViewSet):
    queryset = UserLeave.objects.all()
    serializer_class = UserLeaveSerializer


