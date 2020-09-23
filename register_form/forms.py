from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SubmissionFormModel


class FormSubmissionModel(forms.ModelForm):
    class Meta:
        model = SubmissionFormModel
        fields = '__all__'


class NewUserCreation(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'bg-dark text-light'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'bg-dark text-light'}))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'bg-dark text-light', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'bg-dark text-light', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']
