from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, ToDoList, Category
from .serializers import TaskSerializer, ToDoListSerializer, UserSerializer, CategorySerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == 'GET':
        task = Task.objects.filter(user_id=request.user)
        #task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_get(request, pk):
    try:
        task = Task.objects.filter(user_id=request.user).get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def completed_task_list(request, isComplete):
    task = Task.objects.filter(complete=isComplete, user_id=request.user)
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def completed_task_list_for_todo(request, isComplete, todolist_id):
    try:
        task_list = get_object_or_404(ToDoList, pk=todolist_id, user_id=request.user)
        task = Task.objects.filter(todo_list=task_list, complete=isComplete, user_id=request.user)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    except ToDoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def user_register(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todolist_list(request):
    if request.method == 'GET':
        todolist = ToDoList.objects.filter(user_id=request.user)
        serializer = ToDoListSerializer(todolist, many=True)
        return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todolist_get(request, pk):
    if request.method == 'GET':
        todolist = ToDoList.objects.filter(user_id=request.user).get(pk=pk)
        serializer = ToDoListSerializer(todolist, many=False)
        return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def todolist_create(request):
    serializer = ToDoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def todolist_update(request, pk):
    todolist = get_object_or_404(ToDoListSerializer, pk=pk)
    serializer = ToDoListSerializer(todolist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def todolist_delete(request, pk):
    todolist = get_object_or_404(ToDoList, pk=pk)
    todolist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def todolist_getuserlist(request, user_id):
    if request.method == 'GET':
        todolist = ToDoList.objects.filter(user__id=user_id)
        serializer = ToDoListSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_get(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tasks_for_todolist(request, todolist_id):
    try:
        task_list = get_object_or_404(ToDoList, pk=todolist_id, user_id=request.user)
        tasks = Task.objects.filter(todo_list=task_list, user_id=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    except ToDoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)