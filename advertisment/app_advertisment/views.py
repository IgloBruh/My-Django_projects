from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Это мой первый сайт!!!')

def pobeda(request):
    return HttpResponse('Это мой s сайт!!!')