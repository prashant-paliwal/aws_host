



from attr import field, fields
from django import forms
from matplotlib import widgets
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['students_name','email','password']
        widgets = {
            'students_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class TeacherRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['teachers_name','email','password']


# class TeacherRegistration(StudentRegistration):
#     class Meta(StudentRegistration.Meta):
#         fields = ['teachers_name','email','password']
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control'}),
        #     'password':forms.PasswordInput(attrs={'class':'form-control'}),
        # }