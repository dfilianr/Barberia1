from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['fecha','plan','barbero','horarioAtencion']

        widgets = {
            'plan':    forms.Select(attrs={ 'required': True}),
            'barbero': forms.Select(attrs={ 'required': True}),
            'fecha': forms.SelectDateWidget(attrs={'type':'date','readonly':True}),
            'horarioAtencion': forms.Select(attrs={ 'required': True}),
}