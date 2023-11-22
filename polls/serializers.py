from rest_framework import serializers
from .models import ToDoList, Task, Category, UserProfile
from django.contrib.auth.models import User

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    complete = serializers.BooleanField()
    todo_list = serializers.PrimaryKeyRelatedField(queryset=ToDoList.objects.all())

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        instance.complete = validated_data.get('complete', instance.complete)
        instance.todo_list = validated_data.get('todo_list', instance.todo_list)
        instance.save()
        return instance

class ToDoListSerializer(serializers.ModelSerializer):
    model = ToDoList
    fields = ['id','name','user','category']
    read_only_fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ['id','name']
    read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        print(validated_data)
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['home_address','phone_number']