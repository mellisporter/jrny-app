from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250)
    length = models.CharField(max_length= 100)

    def __str__(self):
        return self.name # prints the workout name