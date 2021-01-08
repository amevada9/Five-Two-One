from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.
class Resturants(models.Model):
    '''
    Here is a model for the resturants. Hopefully as we go on we can store the final choices for people
    in the database, and use the data, time, date, and location (and any other fields we decide on) to create 
    models to predict which resturants are getting service when and where. 

    '''
    name = CharField(max_length=50)
    location = CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
    
