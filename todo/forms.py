""" form for To Do List """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Todo


class TodoForm(forms.ModelForm):
    """ Todo Form """
    class Meta:
        """ fields for Todo form"""
        model = Todo
        fields = ('title', 'description', 'complete')