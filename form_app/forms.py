from .models import FormItems
from django import forms
class Forms1(forms.Form):
    uname =   forms.CharField(widget=forms.TextInput(attrs={'name':'uname'}))
    aadhaar =   forms.DecimalField(widget=forms.NumberInput(attrs={"name":"aadhaar"}))