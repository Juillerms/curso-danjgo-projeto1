from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME1')


def contato(request):
    return HttpResponse('CONTATO2')


def sobre(request):
    return HttpResponse('SOBRE')
