from django.urls import path
from . import views

urlpatterns = [
    path('api/persons/', views.person_list, name='person_list'),
    path('api/persons/<int:pk>/', views.person_detail, name='person_detail'),
    path('api/person_name/', views.person_name, name='person_name'),
    path('api/jobs/', views.job_list, name='job-list'),
    path('api/jobs/<int:pk>/', views.job_detail, name='job-detail'),
]