from django import forms
from .models import TaskGroup, Task

class TaskGroupForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ["group_name"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority", "status", "task_group"]