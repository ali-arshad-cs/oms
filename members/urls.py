from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('create/', views.create_member, name='create_member'),
    path('<int:pk>/', views.member_detail, name='member_detail'),
    path('<int:pk>/update/', views.update_member, name='update_member'),
    path('<int:pk>/delete/', views.delete_member, name='delete_member'),
]
