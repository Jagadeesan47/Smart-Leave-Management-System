from django.urls import path
from .views import apply_leave, leave_status, manage_leaves, approve_leave, reject_leave

urlpatterns = [
    path('apply/', apply_leave, name='apply_leave'),
    path('status/', leave_status, name='leave_status'),
    path('manage/', manage_leaves, name='manage_leaves'),
    path('approve/<int:leave_id>/', approve_leave, name='approve_leave'),
    path('reject/<int:leave_id>/', reject_leave, name='reject_leave'),
]
