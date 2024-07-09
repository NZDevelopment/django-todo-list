from django.urls import path
#from . import views
#from .views import TaskList
from .views import Tasklist, Taskdetail, TaskCreate

urlpatterns = [
    #path('', views.tasklist, name='tasks'),
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
  
]