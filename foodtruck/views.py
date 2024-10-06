from django.shortcuts import render, get_object_or_404
from .models import FoodTruck, FoodTruckEvent
from django.db.models import Q
from datetime import datetime
from django.conf import settings  # Ensure this is imported at the top

# Home page view
def home(request):
    return render(request, 'foodtruck/home.html', {
         
        'MEDIA_URL': settings.MEDIA_URL,  # Pass MEDIA_URL to the template
    })
    



# Truck list view
def truck_list(request):
    trucks = FoodTruck.objects.all()  # Retrieve all food trucks from the database
    return render(request, 'foodtruck/truck_list.html', {'trucks': trucks})

# Event list view
def event_list(request):
    events = FoodTruckEvent.objects.all()  # Retrieve all events from the database
    return render(request, 'foodtruck/event_list.html', {'events': events})

# Search trucks view
def search_trucks(request):
    query = request.GET.get('q', '')  # Get the search query
    trucks = FoodTruck.objects.filter(
        Q(name__icontains=query) | Q(category__icontains=query)
    )  # Filter trucks by name or category
    return render(request, 'foodtruck/search_results.html', {'trucks': trucks, 'query': query})

# Truck calendar view
def truck_calendar(request, truck_id):
    truck = get_object_or_404(FoodTruck, id=truck_id)
    events = FoodTruckEvent.objects.filter(
        food_truck=truck, start_time__gte=datetime.now()
    ).order_by('start_time')  # Retrieve future events for this truck, ordered by date
    return render(request, 'foodtruck/truck_calendar.html', {'truck': truck, 'events': events})



#from django.shortcuts import render
#from .models import FoodTruck

#def truck_list(request):
#    trucks = FoodTruck.objects.all()  # Retrieve all food trucks from the database
#    return render(request, 'foodtruck/truck_list.html', {'trucks': trucks})