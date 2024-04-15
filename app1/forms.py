from django.forms import ModelForm
from .models import Organizer_Model
from django import forms


class EventForm(ModelForm):
    class Meta:
        model=Organizer_Model
        fields='__all__'


        widgets={
            'event_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),

            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True),
           
            'date':forms.TextInput(attrs={'class':'form-control'}),

            'location':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'is_RSVP':forms.TextInput(attrs={'class':'form-control'}),



        }

