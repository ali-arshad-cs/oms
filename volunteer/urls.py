from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.volunteer_list, name='volunteer_list'),
    path('<int:pk>/', views.volunteer_detail, name='volunteer_detail'),
    path('create/', views.create_volunteer, name='create_volunteer'),
    path('<int:pk>/update/', views.update_volunteer, name='update_volunteer'),
    path('<int:volunteer_id>/delete/', views.delete_volunteer, name='delete_volunteer'),
]
