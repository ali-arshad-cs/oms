from django.shortcuts import render

# Create your views here.
# leave/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Leave
from .forms import LeaveForm
from django.contrib import messages


def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'leave/leave_list.html', {'leaves': leaves})


def leave_detail(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    return render(request, 'leave/leave_detail.html', {'leave': leave})


def leave_create(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave request created successfully.')
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'leave/leave_form.html', {'form': form})


def leave_update(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave request updated successfully.')
            return redirect('leave_list')
    else:
        form = LeaveForm(instance=leave)
    return render(request, 'leave/leave_form.html', {'form': form})


def leave_delete(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.delete()
    messages.success(request, 'Leave request deleted successfully.')
    return redirect('leave_list')
