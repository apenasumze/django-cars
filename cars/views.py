from django.shortcuts import render
from django.http import HttpResponse



def cars_view(request):
    return HttpResponse('<h1>Carros</h1>')