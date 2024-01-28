from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Member
from .forms import MemberForm


def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member created successfully!')
            return redirect('members:member_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in field {field}: {error}')
    else:
        form = MemberForm()

    return render(request, 'members/member_form.html', {'form': form})


def update_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member updated successfully.')
            return redirect('members:member_detail', pk=member.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating member: {field.capitalize()} - {error}")
    else:
        form = MemberForm(instance=member)

    return render(request, 'members/member_update.html', {'form': form, 'action': 'Update'})


def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)

    if request.method == 'POST':
        member.delete()
        return redirect('member_list')

    return render(request, 'member_confirm_delete.html', {'member': member})
