from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$',                'pizza.views.home',           name='home'),
    url(r'^pizzas$',          'pizza.views.pizzas',         name='pizzas'),
    url(r'^pizza/new$',       'pizza.views.pizza_new',      name='pizza-new'),
    url(r'^pizza/create$',    'pizza.views.pizza_create',   name='pizza-create'),
)

