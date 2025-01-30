from django.shortcuts import render  
from django.http import HttpResponse  

def home(request):
    return render(request, 'mywebsite_app/home.html')

def about(request):
    return HttpResponse("About will coming as soon")

def projects(request):
    return HttpResponse("Projects will upload as soon as possible")
def weblog(request):
    return HttpResponse("the weblog will comming as soon as possible")

def portfolio(request):
    return HttpResponse("Protfillo will comming as soon as ....")

def contact(request):
    return HttpResponse("the contact will comming as soon as possbile")

def download_resume(request):
    return HttpResponse("The Download will work for Download Resume")