from django.forms import ModelForm
from .models import TaskDetails
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
from django import forms

class TaskDetailsForm(ModelForm):
    class Meta:
        model = TaskDetails
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
       

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


class AddTaskForm(forms.ModelForm):
    class Meta:
        model= TaskDetails
        fields='__all__'
       