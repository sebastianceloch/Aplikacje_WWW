from rest_framework import serializers
from .models import ToDoList, Task, Category, User
class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    complete = serializers.BooleanField(required=False)
    todo_list = serializers.PrimaryKeyRelatedField(queryset=ToDoList.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        instance.complete = validated_data.get('complete', instance.complete)
        instance.todo_list = validated_data.get('todo_list', instance.todo_list)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'name', 'user', 'category']
        read_only_fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password','home_address','phone_number', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        home_address_data = validated_data.pop('home_address', None)
        phone_number_data = validated_data.pop('phone_number', None)
        avatar_data = validated_data.pop('avatar', None)

        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        if home_address_data:
            user.home_address = home_address_data
        if phone_number_data:
            user.phone_number = phone_number_data
        if avatar_data:
            user.avatar = avatar_data
        user.save()
        return user