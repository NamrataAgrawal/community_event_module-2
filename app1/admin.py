from django.contrib import admin
from .models import Organizer_Model
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display=['event_name','email','password','date','location','title','description','is_RSVP']
admin.site.register(Organizer_Model,EventAdmin)