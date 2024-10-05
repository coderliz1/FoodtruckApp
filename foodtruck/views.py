from django.shortcuts import render
from .models import FoodTruck

def truck_list(request):
    trucks = FoodTruck.objects.all()  # Retrieve all food trucks from the database
    return render(request, 'foodtruck/truck_list.html', {'trucks': trucks})
