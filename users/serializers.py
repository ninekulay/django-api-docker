from rest_framework import serializers
from .models import Leave,UserLeave,GetLeave

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('id','title','description')

class GetLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetLeave
        fields = ('leave','user_get','user')

class UserLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLeave
        fields = ('leave','user_leave','user')

