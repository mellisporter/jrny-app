from django.shortcuts import render # allows us to render different views
from django.http import HttpResponse # allows us to get repsonses to Http Requests
from .models import Workout

# Models


#defines our home view
def home(request):
    return render(request, 'home.html') # returns our home template instead of plain text

def about(request):
    return render(request, 'about.html') # changed from text to rendering the about template

def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html' , {'workouts': workouts})

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html' , {'workout' : workout} )

