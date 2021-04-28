from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from .models import Leave,UserLeave
from .views import LeaveViewSet,UserLeaveViewSet

router = routers.DefaultRouter()
router.register('leave',LeaveViewSet)
router.register('user-leave',UserLeaveViewSet)

urlpatterns = [
    path('',include(router.urls)),
]