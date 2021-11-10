from django.urls import path
from task.api.views import (
    task_list,
    api_task_detail,
    api_task_update,
    api_task_delete,
    api_task_create
)

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('task/<int:id>', api_task_detail, name='task-detail'),
    path('task/<int:pk>/update', api_task_update, name="task-update"),
    path('task/<int:pk>/delete', api_task_delete, name="task-delete"),
    path('task/create', api_task_create, name='task-create')
]
