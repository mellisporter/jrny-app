from django.shortcuts import render # allows us to render different views
from django.http import HttpResponse # allows us to get repsonses to Http Requests

#defines our home view
def home(request):
    return render(request, 'home.html') # returns our home template instead of plain text

def about(request):
    return render(request, 'about.html') # changed from text to rendering the about template

def workout_index(request):
    return HttpResponse('this is the workout index')