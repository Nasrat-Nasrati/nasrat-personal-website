from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('weblog',views.weblog, name="weblog"),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('services', views.services,name="services"),
    path('download_resume', views.download_resume, name='download_resume'),
]