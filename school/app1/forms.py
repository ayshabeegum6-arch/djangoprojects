from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import School,Student




class SignupForm(UserCreationForm):
    role_choices = (('student', 'Student'), ('teacher', 'Teacher'))
    role = forms.ChoiceField(choices=role_choices)
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name','role']

    def init(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "_all_"

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','place']
