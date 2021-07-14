from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Wall_Message
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/success')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'wall_messages' : Wall_Message.objects.all()
    }
    return render(request, 'success.html', context)

def post_mess(request):
    if request.method == 'POST':
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id']),
            Wall_Message.objects.create(
                message=request.POST['mess'],
                poster = user
            )
    return redirect ('/success')

def new_func(request):
    return request.session['id']
