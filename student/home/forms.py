from django import forms

from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields= '__all__'
        labels={       
       'student_name': "Student Name",
       'student_phone':"Phone number",
       'student_email':"Email",      
       'student_address':"Address",
       'student_place':"Place",
        }
    