from django.urls import path # allows us to create url paths
from . import views #gives our url file access to the views we have defined

urlpatterns= [
    path('', views.home, name='home'), # our main url path now pulls the home view named home
    path('about/' , views.about, name='about'), # our about path
    path('workouts/', views.workouts_index, name='index'), # index path
    path('workouts/<int:workout_id>/' , views.workouts_detail, name='detail'), # workout detail page
    path('workouts/create/' , views.WorkoutCreate.as_view(), name='workouts_create'), # create workouts path
    path('workouts/<int:pk>/update/' , views.WorkoutUpdate.as_view(), name='workouts_update'), 
    path('workouts/<int:pk>/delete', views.WorkoutDelete.as_view(), name= 'workouts_delete'),
    path('exercises/', views.exercises_index, name='index'),
    path('exercises/<int:exercise_id>/' , views.exercises_detail, name='exercises_detail'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/<int:pk>/update/' , views.ExerciseUpdate.as_view(), name='exercises_update'),
    path('exercises/<int:pk>/delete/' , views.ExerciseDelete.as_view(), name='exercises_delete'),
    path('workouts/<int:workout_id>/add_history/', views.add_history, name='add_history'),
    path('workouts/<int:workout_id>/assoc_exercise/<int:exercise_id>/' , views.assoc_exercise, name='assoc_exercise'), # allows us to view assoc exercises
]