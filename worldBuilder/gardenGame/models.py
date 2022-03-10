from cProfile import label
import datetime
from urllib import request
from django.db import models
import json
from django.contrib.auth.models import User


BUILDING_CHOICES = []
REWARD_CHOICES = [("water_can.png", "water can")]


# Need to implement reward assests in the config file to automatically fetch all possible rewards

# Fetches Building name from the config file, new buildings can be added
# Had some trouble with config path
with open('/Users/vidipkhattar/Downloads/ADjangoApp/worldBuilder/static/config.json') as data_file:
    data = json.load(data_file)
    for item in data['coordinates']:
        BUILDING_CHOICES.append((item['name'], item['name']))


# Database model for registering a building of the day


class buildingOfTheDay(models.Model):

    name = models.CharField(max_length=200, choices=BUILDING_CHOICES)
    description = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    reward = models.CharField(max_length=200, choices=REWARD_CHOICES)


class reportToAdmin(models.Model):
    problem_name = models.CharField(max_length=200)
    problem_description = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='null')
    email = models.CharField(max_length=200, default='null')
