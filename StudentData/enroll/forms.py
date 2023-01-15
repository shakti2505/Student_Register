from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll_no', 'strd']
        labels = {'name':'Enter Student Name',
                 'email':'Enter Email address',
                 'roll_no':'Enter Roll No',
                 'strd':'Group',}

        widgets = { 'name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.TextInput(attrs={'class':'form-control'}),
                    'roll_no':forms.TextInput(attrs={'class':'form-control'}),
                    'strd':forms.TextInput(attrs={'class':'form-control'}),
        }