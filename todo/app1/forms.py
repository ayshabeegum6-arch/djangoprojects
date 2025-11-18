from django import forms
from app1.models import Todo

class AddTaskForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
