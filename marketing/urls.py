from django.urls import path
from . import views

app_name = 'marketing'
urlpatterns = [
    # URLs for PersonLead
    path('person_lead/create/', views.create_person_lead, name='create_person_lead'),
    path('leads/', views.leads_list, name='leads_list'),
    path('person_lead/<int:pk>/update/', views.update_person_lead, name='update_person_lead'),
    path('person_lead/<int:pk>/delete/', views.delete_person_lead, name='delete_person_lead'),

    # URLs for ColdCall
    path('cold_call/create/', views.create_cold_call, name='create_cold_call'),
    path('call_list/', views.calls_list, name='calls_list'),
    path('cold_call/<int:pk>/update/', views.update_cold_call, name='update_cold_call'),
    path('cold_call/<int:pk>/delete/', views.delete_cold_call, name='delete_cold_call'),
]
