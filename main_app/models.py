from django.db import models
from django.urls import reverse # imports reverse functionality

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250)
    length = models.CharField(max_length= 100)

    def __str__(self):
        return self.name # prints the workout name

    def get_absolute_url(self):
        return reverse('detail' , kwargs={'workout_id': self.id}) # builds a path string and returns correct path for the detail route

class Exercise(models.Model): # this will be our second model, exercises can be added to workouts
    name= models.CharField(max_length=50)
    description= models.TextField(max_length=300)
    reps= models.ValueRange

    def __str__(self):
        return self.name