from django.forms import ModelForm
from django import forms
from .models import Patient,PatientInfo

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        widgets = {
            'dateofinfection': forms.DateInput(attrs={'placeholder':'yyyy-mm-dd'})          
        }
        fields = ['name', 'username', 'dateofinfection', 'admited_hospital', 'gender', 'notes','age','address','town','district','state','pin']
        
class PatientInfoForm(ModelForm):
    class Meta:
        model = PatientInfo
        widgets = {
            'notes': forms.Textarea()          
        }
        fields = ['medicine', 'condition', 'notes']