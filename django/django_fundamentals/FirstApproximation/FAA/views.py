from django.shortcuts import render

def index(request):
    return render(request, "index.html")

#def next(request):
    context = {
        "name": request.POST["name"]

    }
    return render(request, "next.html", context)