from django.shortcuts import render # allows us to render different views
from django.http import HttpResponse # allows us to get repsonses to Http Requests
from .models import Workout

# Models

class Workout:
    def __init__(self, name, description, length):
        self.name = name
        self.description = description
        self.length = length

workouts = [
    Workout('Upper Body' , 'Circuit Exercise', '30 mins'),
    Workout('Running' , 'Morning jog' , '30 mins'),
    Workout('Basketball' , 'Pick up at the rec', '60 mins'),
]

#defines our home view
def home(request):
    return render(request, 'home.html') # returns our home template instead of plain text

def about(request):
    return render(request, 'about.html') # changed from text to rendering the about template

def workouts_index(request):
    return render(request, 'workouts/index.html' , {'workouts': workouts})

