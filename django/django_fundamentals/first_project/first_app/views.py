from django.shortcuts import redirect, render, HttpResponse
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs.")

def new(request):
    return HttpResponse("Placeholder to later display a new list of a new blog.")

def create(request):
    return redirect ("/")

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog number: {number}")

def destroy(request, number):
    return redirect ("/")