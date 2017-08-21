from django import forms
from myapp.models import  Student, User


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['username','password','first_name','last_name','email']

class LoginForm(forms.Form):
    username=forms.CharField(label='username')
    password=forms.CharField(widget=forms.PasswordInput)