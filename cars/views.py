from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView
from cars.models import Car
from cars.forms import CarModelForm

# Django Template Language

# Acesso direto pelo ID.
# FIAT = brand.id = 1
# cars = Car.objects.filter(brand=1) 

# Pode-se acessar através da notação __name e utilizar o texto do atributo.
# cars = Car.objects.filter(brand__name='FIAT')

# Filtro parcial (LIKE)
# cars = Car.objects.filter(brand__contains='F')
# cars = Car.objects.filter(brand__icontains='f')  # Ignore case

# Order
# cars = cars.order_by('model') # Ordenação A-Z
# cars = Car.objects.order_by('-model') # Ordenação Z-A
    
# Limit
# cars = Car.objects.all()[:5] # Limita a 5 resultados    


class CarListView(ListView):

    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search: cars = cars.filter(model__contains=search)
        return cars
    

class  NewCarCreateView(CreateView):

    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

