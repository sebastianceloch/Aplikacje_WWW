from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_get),
    path('tasks/create/', views.task_create),
    path('tasks/<int:pk>/update/', views.task_update),
    path('tasks/<int:pk>/delete/', views.task_delete),
    path('tasks/completed/', views.completed_task_list, {'isComplete': True}),
    path('tasks/incomplete/', views.completed_task_list, {'isComplete': False}),
    path('users/register/', views.user_register, name='user_register'),
]

