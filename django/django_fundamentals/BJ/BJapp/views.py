from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "index.html")

def result(request):
    context = {
    	"name": request.POST["name"]
    }
    return render(request, "next.html", context)
    
