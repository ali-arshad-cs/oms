from django.shortcuts import render, get_object_or_404, redirect
from .models import Orphan
from .forms import OrphanForm
from django.contrib import messages
from .utils import title_mapping
from django.contrib.auth.decorators import login_required




@login_required
def orphan_list(request):
    page_title = title_mapping().get('orphan_list', 'Al Saira')

    orphans = Orphan.objects.all()
    onboard_orphans = orphans.filter(status='onboard')
    total_onboard_female_orphans = onboard_orphans.filter(gender='female').count()
    total_onboard_male_orphans = onboard_orphans.filter(gender='male').count()
    total_orphans = orphans.count()
    total_onboard_orphans = orphans.filter(status='onboard').count()

    return render(request, 'orphans/orphan_list.html', {
        'orphans': orphans,
        'total_onboard_female_orphans': total_onboard_female_orphans,
        'total_onboard_male_orphans': total_onboard_male_orphans,
        'total_orphans': total_orphans,
        'total_onboard_orphans': total_onboard_orphans,
        'page_title': page_title,
    })

@login_required
def orphan_detail(request, pk):
    page_title = title_mapping().get('orphan_detail', 'Al Saira')
    orphan = get_object_or_404(Orphan, pk=pk)
    return render(request, 'orphans/orphan_detail.html', {'orphan': orphan, 'page_title': page_title})


@login_required
def orphan_create(request):
    page_title = title_mapping().get('orphan_create', 'Al Saira')
    if request.method == 'POST':
        form = OrphanForm(request.POST, request.FILES)
        if form.is_valid():
            orphan = form.save()
            messages.success(request, 'Orphan created successfully!')
            return redirect('orphans:orphan_detail', pk=orphan.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in field {field}: {error}')
    else:
        form = OrphanForm()

    return render(request, 'orphans/orphan_form.html', {'form': form, 'action': 'Create', 'page_title': page_title})


@login_required
def orphan_update(request, pk):
    orphan = get_object_or_404(Orphan, pk=pk)
    if request.method == 'POST':
        form = OrphanForm(request.POST, instance=orphan)
        if form.is_valid():
            orphan = form.save()
            messages.success(request, 'Orphan updated successfully.')
            return redirect('orphans:orphan_detail', pk=orphan.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating orphan: {field.capitalize()} - {error}")
    else:
        form = OrphanForm(instance=orphan)

    return render(request, 'orphans/orphan_update.html', {'form': form, 'action': 'Update'})


@login_required
def orphan_delete(request, pk):
    try:
        orphan = Orphan.objects.get(pk=pk)
        orphan.delete()
        messages.success(request, 'Orphan deleted successfully.')
    except Orphan.DoesNotExist:
        messages.error(request, 'Orphan not found.')

    return redirect('orphans:orphan_list')
