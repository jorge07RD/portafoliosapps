from noteblock.models import noteblock
from django import forms

from django.forms import ModelForm



class formularionotes(forms.ModelForm):
    class Meta:
        model = noteblock
        fields = '__all__'
        widgets = {
               'color': forms.RadioSelect()
           }