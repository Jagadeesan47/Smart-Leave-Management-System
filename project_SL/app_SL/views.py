from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest
from .forms import LeaveRequestForm

@login_required
def apply_leave(request):
    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user
            leave_request.save()
            return redirect('leave_status')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave/apply_leave.html', {'form': form})

@login_required
def leave_status(request):
    leaves = LeaveRequest.objects.filter(employee=request.user)
    return render(request, 'leave/leave_status.html', {'leaves': leaves})

@login_required
def manage_leaves(request):
    if request.user.is_superuser:
        leaves = LeaveRequest.objects.all()
        return render(request, 'leave/manage_leaves.html', {'leaves': leaves})
    return redirect('leave_status')

@login_required
def approve_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = 'Approved'
    leave.save()
    return redirect('manage_leaves')

@login_required
def reject_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('manage_leaves')

from django.core.mail import send_mail

def approve_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = 'Approved'
    leave.save()
    send_mail('Leave Approved', 'Your leave has been approved.', 'admin@company.com', [leave.employee.email])
    return redirect('manage_leaves')
