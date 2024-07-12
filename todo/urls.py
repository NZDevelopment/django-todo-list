from django.urls import path
#from . import views
#from .views import TaskList
from .views import Tasklist, Taskdetail, TaskUpdate, DeleteView, TaskReorder, CreateTask

urlpatterns = [
    path('', Tasklist.as_view(), name='tasks'),
    path('create_task', CreateTask.as_view(), name='create-task'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task-details'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    #path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task-detail'),
    
  
]