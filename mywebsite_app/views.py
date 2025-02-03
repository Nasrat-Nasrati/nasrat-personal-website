from django.shortcuts import render  
from django.http import HttpResponse  
from .models import About

def home(request):
    return render(request, 'mywebsite_app/home.html')

def about(request):
    about = About.objects.first()
    return render(request,'mywebsite_app/about.html',{'about': about})
    

def projects(request):
    return HttpResponse("Projects will upload as soon as possible")
def weblog(request):
    return HttpResponse("the weblog will comming as soon as possible")

def portfolio(request):
    return HttpResponse("Protfillo will comming as soon as ....")

def contact(request):
    return HttpResponse("the contact will comming as soon as possbile")

def services(request):
    return HttpResponse("the Sevices will come as soon like CV builder website, Online Exam Website, Inforatic Website")

def download_resume(request):
    return HttpResponse("The Download will work for Download Resume")