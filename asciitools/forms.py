from django import forms
from django.core import validators


class ImageToAsciiForm(forms.Form):
    image = forms.ImageField()
    width = forms.NumberInput()
    line_height = forms.FloatField()
