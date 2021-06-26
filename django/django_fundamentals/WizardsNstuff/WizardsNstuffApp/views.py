from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "index.html")
