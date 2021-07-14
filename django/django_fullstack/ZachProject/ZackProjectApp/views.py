from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(name=request.POST['user_name'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/main_page')
    return redirect('/')

def create_giraffe(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = Giraffe.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/main_page')
        else:
            giraffe = Giraffe.objects.create(name=request.POST['giraffe_name'], catchphrase=request.POST['catchphrase'], owner=User.objects.get(id=request.session['user_id']))
            messages.success(request, "Giraffe Successfully Created")
            return redirect('/main_page')
    return redirect('/main_page')

def main_page(request):
    if 'user_id' in request.session:
        context = {
            'current_user': User.objects.get(id=request.session['user_id']),
            'all_giraffes' : Giraffe.objects.all()
        }
        return render(request, "main_page.html", context)
    else:
        return redirect('/')

def profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'profile.html', context)

def show_giraffe(request, giraffe_id):
    if 'user_id' not in request.session:
        return redirect('/')
    giraffes_with_id = Giraffe.objects.filter(id=giraffe_id) 
    if len(giraffes_with_id) == 0:
        return redirect('/main_page')
    context = {
        'one_giraffe' : Giraffe.objects.get(id=giraffe_id),
        }
    return render(request, 'one_giraffe.html', context)

def delete_giraffe(request, giraffe_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        destroyed = Giraffe.objects.get(id=giraffe_id)
        if destroyed.owner.id == request.session['user_id']:
            destroyed.delete()
    return redirect('/main_page')

def login(request):
    if request.method == "POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/main_page')
        messages.error(request, "Email or password is not right")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')