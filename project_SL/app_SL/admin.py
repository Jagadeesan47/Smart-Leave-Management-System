from django.contrib import admin
from .models import EmployeeProfile, LeaveRequest

admin.site.register(EmployeeProfile)
admin.site.register(LeaveRequest)
