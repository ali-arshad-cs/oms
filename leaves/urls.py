# leave/urls.py

from django.urls import path
from .views import leave_list, leave_detail, leave_create, leave_update, leave_delete

urlpatterns = [
    path('list/', leave_list, name='leave_list'),
    path('<int:leave_id>/', leave_detail, name='leave_detail'),
    path('create/', leave_create, name='leave_create'),
    path('<int:leave_id>/update/', leave_update, name='leave_update'),
    path('<int:leave_id>/delete/', leave_delete, name='leave_delete'),
]
