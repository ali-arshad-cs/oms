from django.urls import path
from . import views

urlpatterns = [
    path('', views.orphan_list, name='orphan_list'),
    path('<int:pk>/', views.orphan_detail, name='orphan_detail'),
    path('create/', views.orphan_create, name='orphan_create'),
    path('<int:pk>/update/', views.orphan_update, name='orphan_update'),
    path('<int:pk>/delete/', views.orphan_delete, name='orphan_delete'),
]
