from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User, UserManager
import bcrypt

def log_and_reg(request):
    return render(request, "log_and_reg.html")

def login(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/') 

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['user_id'] = user.id
            messages.success(request, "Sucessfully registered")
            return redirect("/success")
    return redirect ("/")

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, "success.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')
