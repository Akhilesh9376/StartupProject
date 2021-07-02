from App1.models import Contactdata
import App1
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'App1/home.html')

def Team(request):
    return render(request,'App1/team.html')

def Contact(request):
    if request.method=="POST":
        form=Contactdata(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=Contactdata(name=name,email=email,phone=phone,message=message)
        data.save()
                    
        print(name,email,phone,message)
        
    else:
        form=Contactdata()
    return render(request,'App1/contact.html')

def Price(request):
    return render(request,'App1/price.html')

def Blog(request):
    return render(request,'App1/blog.html')
