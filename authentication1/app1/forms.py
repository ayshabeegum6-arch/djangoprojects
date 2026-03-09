from django import forms
from django.contrib.admindocs.views import user_has_model_view_permission
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','phone','address']



#password confirmation
#password encryption



class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)