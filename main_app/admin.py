from django.contrib import admin
from .models import Workout, Exercise # imports workout model


# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)



