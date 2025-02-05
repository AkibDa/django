from django import forms
from .models import OneVarity

class OneVarityForm(forms.Form):
  one_varity = forms.ModelChoiceField(queryset=OneVarity.objects.all(), label="Select one variety")
  