from django.shortcuts import render, redirect # allows us to render different views
from django.http import HttpResponse # allows us to get repsonses to Http Requests
from .models import Workout, Exercise 
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # allows us to use Create and Update functions
from .forms import HistoryForm # takes the form from the history model to embed on our detail page
from django.contrib.auth import login # imports built in login django features
from django.contrib.auth.forms import UserCreationForm # imports default sign up form


# CBVs
class WorkoutCreate(CreateView):
    model= Workout
    fields= ['name' , 'description' , 'length']
    success_url= '/workouts/'

    # if there is a valid workoour form, call this inherited method
    def form_valid(self, form):
        form.instance.user = self.request.user # makes the session user self.request.user
        return super().form_valid(form)

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
    # changed from all to filter to match user
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html' , {'workouts': workouts})

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    history_form= HistoryForm() # history form embeds in the detail
    exercises_workout_doesnt_have = Exercise.objects.exclude(id__in = workout.exercises.all().values_list('id')) # excludes exercises already associated with the workout
    return render(request, 'workouts/detail.html' , {
        'workout' : workout, 'history_form': history_form,
        'exercises': exercises_workout_doesnt_have # we want to display unassociated exercises on the page
        } )


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

def assoc_exercise(request, workout_id, exercise_id):
    Workout.objects.get(id=workout_id).exercises.add(exercise_id)
    return redirect('detail' , workout_id=workout_id)

# i took this straight from the markdown since it says there's no way to really memorize this
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
