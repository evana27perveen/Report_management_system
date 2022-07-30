from django import forms
from .models import *


class ReportModelForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        exclude = ['reporter', 'published_by', 'pre_cat', 'created_on', 'update_date', 'status']


class AssignForm(forms.ModelForm):
    class Meta:
        model = AssignModel
        fields = ['assigned_to', ]
