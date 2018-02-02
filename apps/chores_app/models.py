from __future__ import unicode_literals
from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Child(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    parents = models.ManyToManyField(Parent, related_name = 'children')
    points = models.IntegerField(default = 0)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Chore(models.Model):
    chore = models.CharField(max_length = 255)
    description = models.TextField()
    points = models.IntegerField(default = 0)
    deadline = models.DateTimeField()
    creator = models.ForeignKey(Parent, related_name = 'created_chore')
    children_assigned = models.ManyToManyField(Child, related_name = 'chores_assigned')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
