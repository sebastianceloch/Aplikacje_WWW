from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
    path('tasks/create/', views.task_create),
    path('tasks/<int:pk>/update/', views.task_update),
    path('tasks/<int:pk>/delete/', views.task_delete),
]