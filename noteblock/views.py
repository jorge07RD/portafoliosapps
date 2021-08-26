
from django.http.request import HttpRequest
from django.shortcuts import render,redirect
from noteblock.froms import formularionotes
from noteblock.models import noteblock




# Create your views here.


color = "danger"

def notes (request):

    color = formularionotes()

    notas = noteblock.objects.all()

    return render(request,'notes.html',{'notas':notas})

def buscar(request):
        notas = noteblock.objects.all()

        note = formularionotes(request.POST)
        if note.is_valid():
            note.save()
            note = formularionotes
        return render(request,'notes.html',{'notas':notas})



def delete_event(request,noteblock_id):
    notas = noteblock.objects.all()

    try:
        notes = noteblock.objects.get(id=noteblock_id)
        notes.delete()
        return render(request,'notes.html',{'notas':notas})
        
    except noteblock.DoesNotExist: 
        return render(request,'notes.html',{'notas':notas})