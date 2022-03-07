from dataclasses import field
import datetime
from django import forms
from django.forms import ModelForm
from .models import buildingOfTheDay, reportToAdmin


# Create your forms here.

# From used in the BOTD page to input the building of the day information
class buildingForm(ModelForm):
    class Meta:
        model = buildingOfTheDay
        fields = ('name', 'description', 'date', 'reward')


class reportToAdminForm(ModelForm):
    class Meta:
        model = reportToAdmin
        fields = ('problem_name', 'problem_description', 'username', 'email')
        widgets = {'username': forms.HiddenInput(),
                   'email': forms.HiddenInput()}
