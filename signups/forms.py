from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    student_id = forms.CharField(max_length=9)
    name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['student_id', 'name', 'password1', 'password2']