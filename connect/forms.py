from django import forms
from . import models
from.models import userdetails
class UserForm(forms.ModelForm):
    class Meta:
        model=models.userdetails
        fields='__all__'

class VolunteerForm(forms.ModelForm):
    class Meta:
        model=models.volunteerdetails
        fields='__all__'

from django import forms
from .models import Crisisreporting

class CrisisreportingForm(forms.ModelForm):
    class Meta:
        model = Crisisreporting
        fields = ['message','lat','long', 'location', 'disasterimage', 'affectedpeoples']       

from .models import jobdetails
class JobForm(forms.ModelForm):
    class Meta:
        model = jobdetails
        fields = ['message', 'location', 'vacancy']       


