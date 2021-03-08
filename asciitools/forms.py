from django import forms


class ImageToAsciiForm(forms.Form):
    image = forms.ImageField()
    width = forms.NumberInput()
    line_height = forms.FloatField()


class ImageToEmojiForm(forms.Form):
    image = forms.ImageField()
    width = forms.NumberInput()
    line_height = forms.FloatField()
