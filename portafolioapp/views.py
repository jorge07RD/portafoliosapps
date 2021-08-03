from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import os
import mimetypes
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def index (request):
    return render(request,'index.html')


def contacto(request):

    if request.method=="POST":

        Subject=request.POST["Subject"]
        email_message=request.POST["email"] + " " + request.POST["message"]

        email_from=settings.EMAIL_HOST_USER

        recipiente_list=["jorge.beriguete.mateo@gmail.com"]

        send_mail(Subject,email_message,email_from,recipiente_list)

     
        return render(request,"index.html")
    return render(request,'index.html')    
       
        
  
        
        
