from rest_framework import serializers
from .models import ToDoList, Task


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    todo_list = serializers.PrimaryKeyRelatedField(queryset=ToDoList.objects.all())

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        instance.todo_list = validated_data.get('todo_list', instance.todo_list)
        instance.save()
        return instance

class ToDoListSerializer(serializers.ModelSerializer):
    model = ToDoList
    fields = ['id','name']
    read_only_fields = ['id']