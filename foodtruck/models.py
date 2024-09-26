from django.db import models


class FoodTruck(models.Model):
    name = models.CharField(max_length=100)
    # this is the name of the foodtruck
    category = models.CharField(max_length=100)
    # this is "Mexican", "Brugers", etc

    def __str__(self):
        return self.name
    

class FoodTruckEvent(models.Model):
    food_truck = models.ForeignKey(FoodTruck, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.food_truck.name} at {self.location}"