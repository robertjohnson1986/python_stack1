from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "index.html")

def result(request):
    context = {
    	"why": request.POST["why"],
        "title": request.POST["title"],
        "obvious": request.POST["obvious"],
        "important": request.POST["important"],
        "info": request.POST["info"],
        "support1": request.POST["support1"],
        "case1": request.POST["case1"],
        "support2": request.POST["support2"],
        "case2": request.POST["case2"],
        "support3": request.POST["support3"],
        "case3": request.POST["case3"],
        "well": request.POST["well"],
        "restate": request.POST["restate"],
        "summarize": request.POST["summarize"],
        "added": request.POST["added"],
        "slip": request.POST["slip"]
    }
    return render(request, "next.html", context)
    
