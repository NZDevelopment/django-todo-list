#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, reverse, redirect
#from django.http import HttpResponse
from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #updateview, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #NZ loginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User #Nz remove

from .models import Todo
from .forms import TodoForm


# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction


# Create your views here.


class Tasklist(ListView):
    model = Todo
    context_object_name = 'tasks'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user.id).order_by('-created')

class Taskdetail(DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todo/todo.html'


class CreateTask(View):
    """ add task"""
    def get(self, request):
        """What happens for a GET request"""
        return render(
            request, "todo/create_task.html", {"todo_form": TodoForm()})


    def post(self, request):
        """What happens for a POST request"""
        todo_form = TodoForm(request.POST, request.FILES)

        if todo_form.is_valid():
            form = todo_form.save(commit=False)
            form.user = request.user
            form.save()
            print('save')
            return redirect('tasks')
        else:
            print('error')
            messages.error(self.request, 'Please complete all required fields')
            todo_form = TodoForm()

        return render(
            request,
            "todo/create_task.html",
            {
                "todo_form": todo_form

            },
        )


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Todo #Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


#class TaskUpdate(UpdateView): #Nz attempt. Network error
#    model = Todo
#    form_class = TodoForm
#    template_name = 'todo/create_task.html'  # Use the same template as CreateTask

#    def get_success_url(self):
#        return reverse_lazy('tasks')


def delete_task(request, todo_id):
    """Deletes task"""
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect(reverse(
        'tasks'))



# class DeleteView(LoginRequiredMixin, DeleteView):
#     model = Todo
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks')
#     def get_queryset(self):
#         owner = self.request.user
#         return self.model.objects.filter(user=owner)



class TaskReorder(View): #Reorder
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))    