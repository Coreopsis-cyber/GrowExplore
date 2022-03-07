from cProfile import label
import datetime
from django.db import models

# Create your models here.


class buildingOfTheDay(models.Model):

    building_name = models.CharField(max_length=200)
    buidling_desc = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    reward = models.CharField(max_length=200)
