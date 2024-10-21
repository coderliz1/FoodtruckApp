from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodTruck, FoodTruckEvent
from django.db.models import Q
from datetime import datetime
from django.conf import settings  # Ensure this is imported at the top
from .forms import FoodTruckEventForm



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


# Add event view for truck owners
def add_event(request):
    if request.method == 'POST':
        form = FoodTruckEventForm(request.POST)
        if form.is_valid():
            form.save()  # Save the event to the database
            return redirect('event_list')  # Redirect to the event list page after successful form submission
    else:
        
        form = FoodTruckEventForm()  # Display an empty form for a GET request
        #print(form.start_time.value) this is where a possible problem is at 
        #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        

    return render(request, 'foodtruck/add_event.html', {'form': form})


#from django.shortcuts import render
#from .models import FoodTruck

#def truck_list(request):
#    trucks = FoodTruck.objects.all()  # Retrieve all food trucks from the database
#    return render(request, 'foodtruck/truck_list.html', {'trucks': trucks})