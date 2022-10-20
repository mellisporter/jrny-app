from django.shortcuts import render # allows us to render different views
from django.http import HttpResponse # allows us to get repsonses to Http Requests

#defines our home view
def home(reqest):
    return HttpResponse('<h1>Welcome to JRNY</h1>')

def about(request):
    return HttpResponse('<h1>About JRNY</h1>')

