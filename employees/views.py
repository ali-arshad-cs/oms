# Create your views here.
# employees/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MonthlySalaryForm, EmployeeForm
from .models import Employee, MonthlySalary
from django.contrib import messages


# Employee Views


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('employees:employee_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in field {field}: {error}')
    else:
        form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {'form': form})


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('employees:employee_detail', pk=employee.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error updating employee: {field.capitalize()} - {error}")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/employee_update.html', {'form': form, 'action': 'Update'})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employee_confirm_delete.html', {'employee': employee})


# MonthlySalary Views

def salary_list(request):
    monthly_salaries = MonthlySalary.objects.all()
    return render(request, 'employees/salary_list.html', {'monthly_salaries': monthly_salaries})


def salary_detail(request, salary_id):
    salary = get_object_or_404(MonthlySalary, pk=salary_id)
    return render(request, 'salary_detail.html', {'salary': salary})


def create_salary(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        form = MonthlySalaryForm(request.POST, request.FILES)
        if form.is_valid():
            salary = form.save(commit=False)

            salary.save()
            messages.success(request, 'Salary created successfully.')
            return redirect('employees/salary_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error creating salary: {field.capitalize()} - {error}")
    else:
        form = MonthlySalaryForm()

    return render(request, 'employees/salary_form.html', {'form': form, 'employees': employees})


def update_salary(request, salary_id):
    salary = get_object_or_404(MonthlySalary, pk=salary_id)

    if request.method == 'POST':
        form = MonthlySalaryForm(request.POST, request.FILES, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = MonthlySalaryForm(instance=salary)

    return render(request, 'salary_form.html', {'form': form, 'employee': salary.employee})


def delete_salary(request, salary_id):
    salary = get_object_or_404(MonthlySalary, pk=salary_id)

    if request.method == 'POST':
        salary.delete()
        return redirect('salary_list')

    return render(request, 'monthly_salary_confirm_delete.html', {'salary': salary})
