""" form for To Do List """
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    """ Todo Form """
    class Meta:
        """ fields for Todo form"""
        model = Todo
        fields = ('title', 'description', 'complete')