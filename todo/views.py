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
#def tasklist(request):
#    return HttpResponse('To Do List')
class Tasklist(ListView):
    model = Todo
    context_object_name = 'tasks'

class Taskdetail(DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todo/todo.html'


# class TaskCreate(CreateView):
#     model = Todo
#     fields = '__all__'
#     success_url = reverse_lazy('tasks')


#@login_required
#@method_decorator(login_required, name='dispatch')
#class TaskCreate(View):
#class TaskCreate(LoginRequiredMixin, CreateView):
    #""" add recipe"""
 #   @login_required
#    def get(self, request):
#        """What happens for a GET request"""
#        return render(
#            request, "todo/todo_form.html", {"todo_form": TodoForm()})
#    @login_required
#    def post(self, request):
#        """What happens for a POST request"""
#        todo_form = TodoForm(request.POST, request.FILES)

#        if todo_form.is_valid():
#            todo = todo_form.save(commit=False)        
#            todo.author = request.user
            #todo.slug = slugify('-'.join([todo.title, str(todo.author)]), allow_unicode=False)
            #form.instance.user = self.request.user #Nz remove
#            todo.author = request.user #Nz remove after testing
#            todo_form.instance.description = todo.description
#            todo.save()
#            messages.success(request, " Task added successfully!") #Nz
 #           return redirect('tasks')
#        else:
#            messages.error(self.request, 'Please complete all required fields')
#            todo_form = TodoForm()

#        return render(
#            request,
#            "todo/todo_form.html",
#            {"todo_form": todo_form},
#        )

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)





# Nz
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Todo #Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)



class TaskReorder(View): #Reorder
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))    