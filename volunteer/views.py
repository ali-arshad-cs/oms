from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Volunteer
from .forms import VolunteerForm


def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/volunteer_list.html', {'volunteers': volunteers})


def volunteer_detail(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    return render(request, 'volunteers/volunteer_detail.html', {'volunteer': volunteer})


def create_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Volunteer created successfully!')
            return redirect('volunteers:volunteer_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in field {field}: {error}')
    else:
        form = VolunteerForm()

    return render(request, 'volunteers/volunteer_form.html', {'form': form})


def update_volunteer(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)

    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES, instance=volunteer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Volunteer updated successfully.')
            return redirect('volunteers:volunteer_detail', pk=volunteer.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating volunteer: {field.capitalize()} - {error}")
    else:
        form = VolunteerForm(instance=volunteer)

    return render(request, 'volunteers/volunteer_update.html', {'form': form, 'action': 'Update'})


def delete_volunteer(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)

    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteer_list')

    return render(request, 'volunteer_confirm_delete.html', {'volunteer': volunteer})
