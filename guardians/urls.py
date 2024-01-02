# guardians/urls.py
from django.urls import path
from . import views

app_name = 'guardians'

urlpatterns = [
    path('list/', views.guardian_list, name='guardian_list'),
    path('<int:pk>/', views.guardian_detail, name='guardian_detail'),
    path('create/', views.guardian_create, name='guardian_create'),
    path('<int:pk>/update/', views.guardian_update, name='guardian_update'),
    path('<int:pk>/delete/', views.guardian_delete, name='guardian_delete'),
]