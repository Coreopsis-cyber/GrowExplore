# Generated by Django 4.0.3 on 2022-03-06 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buildingOfTheDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=200)),
                ('buidling_desc', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]