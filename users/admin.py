from django.contrib import admin
from .models import Leave,UserLeave

admin.site.register(Leave)


class UserLeaveAdmin(admin.ModelAdmin):
	list_display = ['leave','user_leave','user']

admin.site.register(UserLeave,UserLeaveAdmin)