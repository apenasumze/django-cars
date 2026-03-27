from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from cars.models import Car
from cars.forms import CarModelForm


def cars_view(request: HttpRequest) -> HttpResponse:
    # Django Template Language
    
    # Todos os carros
    cars = Car.objects.all() 
    
    search = request.GET.get('search')
    if search:
        print(search)
        cars = cars.filter(model__contains=search)

    
    # Acesso direto pelo ID.
    # FIAT = brand.id = 1
    # cars = Car.objects.filter(brand=1) 
    
    # Pode-se acessar através da notação __name e utilizar o texto do atributo.
    # cars = Car.objects.filter(brand__name='FIAT')
    
    # Filtro parcial (LIKE)
    # cars = Car.objects.filter(brand__contains='F')
    # cars = Car.objects.filter(brand__icontains='f')  # Ignore case
    
    # Order
    cars = cars.order_by('model') # Ordenação A-Z
    # cars = Car.objects.order_by('-model') # Ordenação Z-A
    
    

    print(cars)

    return render(
        request, 
        'cars.html',
        context={'cars': cars}
        )
    
    
def new_car_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            print(new_car_form)
            return redirect('cars_list')
    
    else:
        new_car_form = CarModelForm()
        
    return render(request, 'new_car.html', context={'new_car_form': new_car_form})