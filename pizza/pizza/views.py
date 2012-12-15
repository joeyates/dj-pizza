from django import http
from django.shortcuts import render

from pizza.models import *

def home(request):
    html = "<h1>Hello World!</h1>"
    return http.HttpResponse(html)

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizza/pizzas.html', context)

