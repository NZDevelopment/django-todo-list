from django.urls import path
#from . import views
#from .views import TaskList
from .views import Tasklist, Taskdetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder

urlpatterns = [
    #path('', views.tasklist, name='tasks'),
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='tasks'),
    path('task_create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    #path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task-detail'),
  
]