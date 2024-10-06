from django.contrib import admin
from .models import FoodTruck, FoodTruckEvent 



# Define admin class for FoodTruck
class FoodTruckAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Show name and category in the admin list view
    search_fields = ('name', 'category')  # Allow search by name and category

# Define admin class for FoodTruckEvent
class FoodTruckEventAdmin(admin.ModelAdmin):
    list_display = ('food_truck', 'location', 'start_time', 'end_time')  # Show these fields in the admin list view
    list_filter = ('food_truck', 'location')  # Add filters for food truck and location
    search_fields = ('food_truck__name', 'location')  # Allow search by food truck name and location

# Register models with the customized admin classes
admin.site.register(FoodTruck, FoodTruckAdmin)
admin.site.register(FoodTruckEvent, FoodTruckEventAdmin)









#admin.site.register(FoodTruck)
#admin.site.register(FoodTruckEvent)