# employees/urls.py

from django.urls import path
from .views import (employee_list, employee_detail, create_employee, update_employee, delete_employee,
                    salary_list, salary_detail, create_salary, update_salary, delete_salary)
app_name = 'employees'
urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),
    path('employees/create/', create_employee, name='employee_create'),
    path('employees/<int:pk>/update/', update_employee, name='employee_update'),
    path('employees/<int:pk>/delete/', delete_employee, name='employee_delete'),
    path('salaries/', salary_list, name='salary_list'),
    path('salaries/<int:pk>/', salary_detail, name='salary_detail'),
    path('salaries/create/', create_salary, name='salary_create'),
    path('salaries/<int:pk>/update/', update_salary, name='salary_update'),
    path('salaries/<int:pk>/delete/', delete_salary, name='salary_delete'),
]