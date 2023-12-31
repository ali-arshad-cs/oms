from django.shortcuts import render, get_object_or_404, redirect
from .models import Orphan
from .forms import OrphanForm
from django.contrib import messages

def orphan_list(request):
    orphans = Orphan.objects.all()
    return render(request, 'orphans/orphan_list.html', {'orphans': orphans})


def orphan_detail(request, pk):
    orphan = get_object_or_404(Orphan, pk=pk)
    return render(request, 'orphans/orphan_detail.html', {'orphan': orphan})




def orphan_create(request):
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

    return render(request, 'orphans/orphan_form.html', {'form': form, 'action': 'Create'})



def orphan_update(request, pk):
    orphan = get_object_or_404(Orphan, pk=pk)
    if request.method == 'POST':
        form = OrphanForm(request.POST, instance=orphan)
        if form.is_valid():
            orphan = form.save()
            return redirect('orphans:orphan_detail', pk=orphan.pk)
    else:
        form = OrphanForm(instance=orphan)
    return render(request, 'orphans/orphan_update.html', {'form': form, 'action': 'Update'})


def orphan_delete(request, pk):
    orphan = get_object_or_404(Orphan, pk=pk)
    orphan.delete()
    return redirect('orphan_list')
