from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import User

def log_and_reg (request):
    return render (request, 'index.html')

def login(request):
    return render(request, "success.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name = request.POST['first_name'], last_name =request.POST['last_name'], email=request.POST['email'], password=pw_hash
            )
            messages.success(request, "Successfully registered")
            request.session['user_id'] = user.id
        return redirect("/success")
    return redirect('/')

def success(request):
    if not "user_id" in request.session:
        return redirect("/")
    context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
    return render(request,"success.html", context)

def logout(request):
    request.session.flush()
    return redirect ('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email']) 
        if user:
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                messages.success(request, "Successfully logged in!")
                return redirect('/success')
            messages.error(request, "Inccorrect email/password combination")
        else:
            messages.error(request, "Email could not be found in database")
    return redirect("/")    