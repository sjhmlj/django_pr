from pyexpat import model
from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=80)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)


class myTodo(models.Model):
    content = models.CharField(max_length=80)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)


class myTodo_bt(models.Model):
    content = models.CharField(max_length=80)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    edit = models.IntegerField(null=True)
    id_2 = models.IntegerField(default=0)
