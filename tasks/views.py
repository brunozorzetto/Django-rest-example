from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Task
from rest_framework import viewsets
from .Serializers import TaskSerializer, UserSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created')
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer