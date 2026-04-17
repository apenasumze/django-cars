from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class  NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'