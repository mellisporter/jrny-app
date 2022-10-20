from django.urls import path # allows us to create url paths
from . import views #gives our url file access to the views we have defined

urlpatterns= [
    path('', views.home, name='home'), # our main url path now pulls the home view named home
    path('about/' , views.about, name='about'), # our about path
    path('workouts/', views.workouts_index, name='index'), # index path
    path('workouts/<int:workout_id>/' , views.workouts_detail, name='detail'), # workout detail page
    path('workouts/create/' , views.WorkoutCreate.as_view(), name='workouts_create'), # create workouts path
]