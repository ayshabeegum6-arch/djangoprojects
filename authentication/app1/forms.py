from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import UserCreationsForm
from app1.models
class SignupForm(UserCreationForm):


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2,'email','first_name','last_name']



class LoginForm(forms.form):
            username=forms.CharField(max_length=20)
            password=forms.CharField(max_length=20)




