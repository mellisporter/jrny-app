from django.urls import path # allows us to create url paths
from . import views #gives our url file access to the views we have defined

urlpatterns= [
    path('', views.home, name='home'), # our main url path now pulls the home view named home
    path('about/' , views.about, name='about'),
]