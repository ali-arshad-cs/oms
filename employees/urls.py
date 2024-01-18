# employees/urls.py

from django.urls import path
from .views import employee_list, employee_detail, create_employee, update_employee, delete_employee
app_name = 'employees'
urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),
    path('employees/create/', create_employee, name='employee_create'),
    path('employees/<int:pk>/update/', update_employee, name='employee_update'),
    path('employees/<int:pk>/delete/', delete_employee, name='employee_delete'),
]