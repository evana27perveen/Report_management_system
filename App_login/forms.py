from django import forms
from .models import *
from django.contrib.auth import forms as auth_form


class HODUserForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class HODForm(forms.ModelForm):
    class Meta:
        model = HeadOfDepartmentModel
        exclude = ['user', 'designation', 'joining_date', 'status']


class OfficerUserForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class OfficerForm(forms.ModelForm):
    class Meta:
        model = OfficerModel
        exclude = ['user', 'designation', 'joining_date', 'status']


class ReporterUserForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ReporterForm(forms.ModelForm):
    class Meta:
        model = ReporterModel
        exclude = ['user', 'designation', 'joining_date', 'status']
