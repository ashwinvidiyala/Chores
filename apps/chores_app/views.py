from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import *

def index(request):
    return render(request, 'chores_app/index.html')

def add_child(request):
    pass
