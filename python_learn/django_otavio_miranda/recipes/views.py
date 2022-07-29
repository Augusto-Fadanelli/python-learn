from django.http import HttpResponse # Retorna um response genérico
#from django.shortcuts import render

def home(request):
    return HttpResponse('HOME')

def contato(request):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')


