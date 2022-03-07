from dataclasses import field
import datetime
from django import forms
from django.forms import ModelForm
from .models import buildingOfTheDay


# Create your forms here.

class buildingForm(ModelForm):
    class Meta:
        model = buildingOfTheDay
        fields = ('building_name', 'buidling_desc', 'date', 'reward')

    CHOICES = [('Harrison Building', 'Harrison Building'),
               ('Amory Building', 'Amory Building'),
               ('select3', 'select 3'),
               ('select4', 'select 4'),
               ('select5', 'select 5'),
               ('select6', 'select 6'),
               ('select7', 'select 7'),
               ('select8', 'select 8'),
               ('select9', 'select 9'),
               ('select10', 'select 10'),
               ('select11', 'select 11')]
    building_name = forms.ChoiceField(
        label="Building Name", choices=CHOICES, widget=forms.RadioSelect)
    buidling_desc = forms.CharField(label="Description", max_length=200)
    date = forms.DateField(initial=datetime.date.today)
    reward = forms.CharField(label="Daily Reward", max_length=200)
