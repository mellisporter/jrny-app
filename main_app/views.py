from django.shortcuts import render, redirect # allows us to render different views
from django.http import HttpResponse # allows us to get repsonses to Http Requests
from .models import Workout, Exercise 
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # allows us to use Create and Update functions
from .forms import HistoryForm # takes the form from the history model to embed on our detail page
# CBVs
class WorkoutCreate(CreateView):
    model= Workout
    fields= '__all__'
    success_url= '/workouts/'

class WorkoutUpdate(UpdateView):
    model= Workout
    fields= '__all__'

class WorkoutDelete(DeleteView):
    model= Workout
    success_url= '/workouts/'

class ExerciseList(ListView):
    model= Exercise

class ExerciseCreate(CreateView):
    model= Exercise
    fields= '__all__'
    success_url= '/exercises/'

class ExerciseUpdate(UpdateView):
    model= Exercise
    fields= '__all__'

class ExerciseDelete(DeleteView):
    model= Exercise
    success_url= '/exercises/'



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
    history_form= HistoryForm() # history form embeds in the detail
    return render(request, 'workouts/detail.html' , {'workout' : workout, 'history_form': history_form} )

def exercises_index(request):
    exercises= Exercise.objects.all()
    return render(request, 'exercises/index.html', {'exercises' : exercises})

def exercises_detail(request, exercise_id):
    exercises= Exercise.objects.get(id=exercise_id)
    return render(request, 'exercises/detail.html', {'exercise': exercises})

def add_history(request, workout_id):
    form= HistoryForm(request.POST)
    if form.is_valid():
        new_history= form.save(commit=False)
        new_history.workout_id = workout_id
        new_history.save()
    return redirect('detail' , workout_id=workout_id)