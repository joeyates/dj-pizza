from django import http
from django.shortcuts import redirect, render

from pizza.forms import *
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

def pizza_new(request):
    context = {
        'form': PizzaForm(),
    }
    return render(request, 'pizza/pizza-new.html', context)

def pizza_create(request):
    if request.method != 'POST':
        return http.HttpResponseBadRequest()
    form = PizzaForm(data=request.POST)
    if not form.is_valid():
        return http.HttpResponseBadRequest()
    pizza = Pizza(
        name = form.cleaned_data['name'],
        description = form.cleaned_data['description']
    )
    pizza.save()
    return redirect('pizzas')

