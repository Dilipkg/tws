from django.urls import path
from .views import (
    RegisterView,
    TaskCreateView,
    TaskListView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    AddTaskMemberView,
    RemoveTaskMemberView,
    TaskMembersListView,
    UpdateTaskStatusView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:task_id>/members/', TaskMembersListView.as_view(), name='task-members'),
    path('tasks/add-member/', AddTaskMemberView.as_view(), name='add-task-member'),
    path('tasks/remove-member/', RemoveTaskMemberView.as_view(), name='remove-task-member'),
    path('tasks/update-status/', UpdateTaskStatusView.as_view(), name='update-task-status'),
]
