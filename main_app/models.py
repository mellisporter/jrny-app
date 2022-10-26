from django.db import models
from django.urls import reverse # imports reverse functionality
from django.contrib.auth.models import User # allows us to use built in user models from Django

# Create your models here.
# need to move exercise here so Workout recognizes it below
class Exercise(models.Model): # this will be our second model, exercises can be added to workouts
    name= models.CharField(max_length=50)
    description= models.TextField(max_length=300)
    reps= models.IntegerField

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercises_detail' , kwargs={'exercise_id': self.id}) # builds a path string and returns correct path for the detail route

class Workout(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250)
    length = models.CharField(max_length= 100)
    exercises = models.ManyToManyField(Exercise) # links exercises to workout model as many to many
    user = models.ForeignKey(User, on_delete=models.CASCADE) # makes it so when a user is delete, the asociated info does as well

    def __str__(self):
        return self.name # prints the workout name

    def get_absolute_url(self):
        return reverse('detail' , kwargs={'workout_id': self.id}) # builds a path string and returns correct path for the detail route

class History(models.Model):
    date= models.DateField('Workout Date')
    time= models.TimeField()
    notes= models.TextField(max_length=300)

    # the history model needs at workout FK
    # this makes it so the history attaches to a certain workout
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f'Workout comopleted on {self.date}'

    class Meta:
        ordering= ['-date']