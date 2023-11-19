from django.urls import path
from . import views

urlpatterns = [
    path('api/persons/', views.person_list, name='person_list'),
    path('api/persons/<int:pk>/', views.person_detail),
    path('api/update/', views.person_update),
    path('api/delete', views.person_delete),
    path('api/jobs/', views.job_list, name='job-list'),
    path('api/jobs/<int:pk>/', views.job_detail, name='job-detail'),
    path('api/jobs/<int:job_id>/members/', views.job_members, name='job-members'),
]