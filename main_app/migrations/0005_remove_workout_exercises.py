# Generated by Django 4.1.2 on 2022-10-20 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_history_options_workout_exercises_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='exercises',
        ),
    ]
