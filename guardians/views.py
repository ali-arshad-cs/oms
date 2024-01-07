# guardians/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Guardian
from .forms import GuardianForm  # Create a form for Guardian if needed
from django.contrib import messages


def guardian_list(request):
    guardians = Guardian.objects.all()
    sorted_guardians = sorted(guardians, key=lambda x: x.first_name)
    return render(request, 'guardians/guardian_list.html', {'guardians': sorted_guardians})


def guardian_detail(request, pk):
    guardian = get_object_or_404(Guardian, pk=pk)
    return render(request, 'guardians/guardian_detail.html', {'guardian': guardian})


def guardian_create(request):
    if request.method == 'POST':
        form = GuardianForm(request.POST, request.FILES)
        if form.is_valid():
            guardian = form.save()
            messages.success(request, 'Guardian created successfully!')
            return redirect('guardians:guardian_detail', pk=guardian.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error creating guardian: {field.capitalize()} - {error}")
    else:
        form = GuardianForm()

    return render(request, 'guardians/guardian_form.html', {'form': form, 'action': 'Create'})


def guardian_update(request, pk):
    guardian = get_object_or_404(Guardian, pk=pk)

    if request.method == 'POST':
        form = GuardianForm(request.POST, request.FILES, instance=guardian)
        if form.is_valid():
            guardian = form.save()
            messages.success(request, 'Guardian updated successfully.')
            return redirect('guardians:guardian_detail', pk=guardian.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating guardian: {field.capitalize()} - {error}")
    else:
        form = GuardianForm(instance=guardian)

    return render(request, 'guardians/guardian_update.html', {'form': form, 'action': 'Update'})



def guardian_delete(request, pk):
    try:
        guardian = Guardian.objects.get(pk=pk)
        guardian.delete()
        messages.success(request, 'Guardian deleted successfully.')
    except Guardian.DoesNotExist:
        messages.error(request, 'Guardian not found.')

    return redirect('guardians:guardian_list')
