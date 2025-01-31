
from .models import Coffee
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee/index.html', {'coffees': coffees})


def show(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    print(coffee)
    return render(request, 'coffee/show.html', {'coffee': coffee})
    


