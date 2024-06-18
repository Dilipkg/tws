from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task, TaskMember
from .serializers import TaskSerializer, UserSerializer, TaskMemberSerializer

# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

# Create Task
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

# Read Tasks
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update Task
class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete Task
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

# Add/Remove Task Members
class AddTaskMemberView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        task_id = request.data.get('task_id')
        user_id = request.data.get('user_id')
        task = Task.objects.get(id=task_id)
        user = User.objects.get(id=user_id)
        TaskMember.objects.create(task=task, user=user)
        return Response(status=status.HTTP_201_CREATED)

class RemoveTaskMemberView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        task_id = request.data.get('task_id')
        user_id = request.data.get('user_id')
        task = Task.objects.get(id=task_id)
        user = User.objects.get(id=user_id)
        TaskMember.objects.filter(task=task, user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View Task Members
class TaskMembersListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, task_id, *args, **kwargs):
        task_members = TaskMember.objects.filter(task_id=task_id)
        serializer = TaskMemberSerializer(task_members, many=True)
        return Response(serializer.data)

# Update Task Status
class UpdateTaskStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        task_id = request.data.get('task_id')
        status = request.data.get('status')
        task = Task.objects.get(id=task_id)
        task.status = status
        task.save()
        return Response(TaskSerializer(task).data)
