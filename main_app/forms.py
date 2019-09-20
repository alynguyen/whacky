from django.forms import ModelForm
from .models import Widget
from django import forms

class WidgetForm(forms.ModelForm):
  class Meta:
    model = Widget
    fields = '__all__'