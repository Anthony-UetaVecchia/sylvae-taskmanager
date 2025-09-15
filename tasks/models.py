from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q, F
from django.core.exceptions import ValidationError

class TaskGroup(models.Model):
    user=models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='task_groups'
    )

    group_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta():
        unique_together=('user', 'group_name')
        ordering=['group_name']

    def __str__(self):
        return f"{self.group_name} ({self.user.username})"
    
class Task(models.Model):
    user=models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks'
    )
    task_group=models.ForeignKey(
        TaskGroup, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks'
    )

    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    due_date=models.DateField(null=True, blank=True)
    PRIORITY_CHOICES=[
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    priority=models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    STATUS_CHOICES=[
        ("todo", "To do"),
        ("doing", "Doing"),
        ("done", "Done"),
    ]
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        indexes=[
            models.Index(fields=['user','status']),
        ]
        ordering=['-created_at']

    def clean(self):
        """Custom validation to ensure the group belongs to the same user as the task."""
        if self.task_group and self.task_group.user_id != self.user_id:
            raise ValidationError({
                'task_group': "Group has to belong to the same task user",
            })

    def __str__(self):
        return self.title