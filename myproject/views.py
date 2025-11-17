from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World first django page")

def about(request):
    return HttpResponse("This is the about page")
