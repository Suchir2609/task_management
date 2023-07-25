from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['status']

# class TaskCreationForm(forms.ModelForm):
#
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'status']