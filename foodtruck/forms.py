from django import forms
from .models import FoodTruckEvent

class FoodTruckEventForm(forms.ModelForm):
    class Meta:
        model = FoodTruckEvent
        
        start_time=forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
        fields = ['food_truck', 'location', 'start_time', 'end_time', 'event_name', 'date']
