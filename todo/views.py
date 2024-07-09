from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm

# Create your views here.
#def tasklist(request):
#    return HttpResponse('To Do List')
class Tasklist(ListView):
    model = Todo
    context_object_name = 'tasks'

class Taskdetail(DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todo/todo.html'


class TaskCreate(CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskCreate(View):
    """ add recipe"""
    def get(self, request):
        """What happens for a GET request"""
        return render(
            request, "todo/todo_form.html", {"todo_form": TodoForm()})
