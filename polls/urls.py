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
    path('todolist/', views.todolist_list),
    path('todolist/<int:pk>/', views.todolist_get),
    path('todolist/create/', views.todolist_create),
    path('todolist/<int:pk>/update/', views.todolist_update),
    path('todolist/<int:pk>/delete/', views.todolist_delete),
    path('todolist/user/<int:user_id>/', views.todolist_getuserlist),
    path('category/<int:pk>/', views.category_get),
    path('category/create/', views.category_create),
    path('category/<int:pk>/update/', views.category_update),
    path('category/<int:pk>/delete/', views.category_delete),
    path('tasklist/<int:todolist_id>/', views.tasks_for_todolist),
    path('tasks/completed/<int:todolist_id>/', views.completed_task_list_for_todo, {'isComplete': True}),
    path('tasks/incomplete/<int:todolist_id>/', views.completed_task_list_for_todo, {'isComplete': False}),
]

