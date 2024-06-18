from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, TaskMember

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'created_at', 'updated_at']

class TaskMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskMember
        fields = ['id', 'task', 'user']
