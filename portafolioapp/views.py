from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import os
import mimetypes
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


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
        messages.add_message(request, messages.INFO, 'mensaje enviado.')
     
        return HttpResponseRedirect('enviar')


def enviar (request):
    return render(request,'index.html')
       
        
  
        
        
