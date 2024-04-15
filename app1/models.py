from django.db import models
from django.utils import timezone
# import datetime



# Create your models here.

class Organizer_Model(models.Model):
    event_name=models.CharField(max_length=500,null=True)
    email=models.EmailField(max_length=60,null=True)
    password=models.CharField(max_length=12,null=True)
    date=models.DateTimeField(auto_now_add=True,verbose_name='Date & Time')
    location=models.CharField(max_length=25,null=True,blank=True)
    title=models.CharField(max_length=25,null=True,blank=True)
    description=models.CharField(max_length=25,null=True,blank=True)
    is_RSVP=models.BooleanField(default=False)

    def __str__(self) :
        return self.name