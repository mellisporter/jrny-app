# Generated by Django 4.1.2 on 2022-10-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_workout_exercises'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(to='main_app.exercise'),
        ),
    ]
