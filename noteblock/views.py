from django.urls import reverse
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from noteblock.froms import formularionotes
from noteblock.models import noteblock




# Create your views here.


color = "danger"

def notes (request):

    notas = noteblock.objects.all()

    return render(request,'notes.html',{'notas':notas})

def save_note(request):
        notas = noteblock.objects.all()

        note = formularionotes(request.POST)
        if note.is_valid():
            note.save()
            return HttpResponseRedirect('notes',{'notas':notas})

def save_note_guarda (request):

    notas = noteblock.objects.all()

    return render(request,'notes.html',{'notas':notas})




           



def delete_event(request,noteblock_id):
    notas = noteblock.objects.all()

    try:
        notes = noteblock.objects.get(id=noteblock_id)
        notes.delete()
        return render(request,'notes.html',{'notas':notas})
        
    except noteblock.DoesNotExist: 
        return render(request,'notes.html',{'notas':notas})