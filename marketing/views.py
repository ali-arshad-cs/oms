from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PersonLead, ColdCall
from .forms import PersonLeadForm, ColdCallForm


def create_person_lead(request):
    if request.method == 'POST':
        form = PersonLeadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person lead created successfully.')
            return redirect('marketing:leads_list')  # Redirect to lead list page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error creating person lead: {field.capitalize()} - {error}")
    else:
        form = PersonLeadForm()
    return render(request, 'marketing/create_person_lead.html', {'form': form})


def leads_list(request):
    leads = PersonLead.objects.all()
    return render(request, 'marketing/lead_list.html', {'leads': leads})


def update_person_lead(request, pk):
    person_lead = get_object_or_404(PersonLead, pk=pk)
    if request.method == 'POST':
        form = PersonLeadForm(request.POST, request.FILES, instance=person_lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person lead updated successfully.')
            return redirect('marketing:leads_list')  # Redirect to lead list page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating person lead: {field.capitalize()} - {error}")
    else:
        form = PersonLeadForm(instance=person_lead)
    return render(request, 'marketing/update_person_lead.html', {'form': form})


def delete_person_lead(request, pk):
    person_lead = get_object_or_404(PersonLead, pk=pk)
    if request.method == 'POST':
        person_lead.delete()
        messages.success(request, 'Person lead deleted successfully.')
        return redirect('lead_list')  # Redirect to lead list page
    return render(request, 'delete_person_lead.html', {'person_lead': person_lead})


def create_cold_call(request):
    if request.method == 'POST':
        form = ColdCallForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cold call created successfully.')
            return redirect('marketing:calls_list')  # Redirect to cold call list page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error creating cold call: {field.capitalize()} - {error}")
    else:
        form = ColdCallForm()
    return render(request, 'marketing/create_cold_call.html', {'form': form})


def calls_list(request):
    calls = ColdCall.objects.all()
    return render(request, 'marketing/cold_call_list.html', {'calls': calls})


def update_cold_call(request, pk):
    cold_call = get_object_or_404(ColdCall, pk=pk)
    if request.method == 'POST':
        form = ColdCallForm(request.POST, instance=cold_call)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cold call updated successfully.')
            return redirect('cold_call_list')  # Redirect to cold call list page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating cold call: {field.capitalize()} - {error}")
    else:
        form = ColdCallForm(instance=cold_call)
    return render(request, 'update_cold_call.html', {'form': form})


def delete_cold_call(request, pk):
    cold_call = get_object_or_404(ColdCall, pk=pk)
    if request.method == 'POST':
        cold_call.delete()
        messages.success(request, 'Cold call deleted successfully.')
        return redirect('cold_call_list')  # Redirect to cold call list page
    return render(request, 'delete_cold_call.html', {'cold_call': cold_call})
