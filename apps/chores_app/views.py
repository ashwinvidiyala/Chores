from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import *

def index(request):
    return render(request, 'chores_app/index.html')

def register(request):
    if request.POST['submit'] == 'Register':
        errors = parent.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags = tag)
            return redirect('/index')

        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        parent = Parent.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        if 'id' not in request.session:
            request.session['id'] = parent.id
        else:
            request.session['id'] = parent.id

def login(request):
    if request.POST['submit'] == 'Login':
        parent = Parent.objects.filter(email = request.POST['email'])
        if not parent:
            messages.add_message(request, messages.INFO, 'Parent does not exist')
            return redirect('/index')
        else:
            for parent in parent:
                parent_password = parent.password
            if bcrypt.checkpw(request.POST['password'].encode(), parent_password.encode()):
                if 'id' not in request.session:
                    request.session['id'] = parent.id
                else:
                    request.session['id'] = parent.id
                return redirect('/parent/show/'+str(request.session['id']))
            else:
                messages.add_message(request, messages.INFO, 'Password is incorrect')
                return redirect('/index')
