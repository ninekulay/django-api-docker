from rest_framework import serializers
from .models import Leave,UserLeave

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('id','title','description')

class UserLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLeave
        fields = ('leave','user_leave','user')

