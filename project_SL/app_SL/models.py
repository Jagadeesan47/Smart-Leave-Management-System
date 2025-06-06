from django.db import models
from django.contrib.auth.models import User

# Employee Profile
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Employee', 'Employee')])

    def __str__(self):
        return self.user.username

# Leave Model
class LeaveRequest(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, choices=[('Sick', 'Sick'), ('Casual', 'Casual')])
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type}"
