from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from .models import Leave,UserLeave,GetLeave
from .views import LeaveViewSet,UserLeaveViewSet,GetLeaveViewSet

router = routers.DefaultRouter()
router.register('leave',LeaveViewSet)
router.register('user-leave',UserLeaveViewSet)
router.register('user-data',GetLeaveViewSet)

urlpatterns = [
    path('',include(router.urls)),
]