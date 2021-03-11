from django import forms


class ImageToAsciiForm(forms.Form):
    image = forms.ImageField()
    width = forms.IntegerField()
    character_width = forms.FloatField()
    line_height = forms.FloatField()
    symbols = forms.CharField()

    def clean_width(self):
        data = self.cleaned_data.get("width")

        if data > 800 or data < 8:
            raise forms.ValidationError("Pick a value between 8 and 800")

        return data

    def clean_character_width(self):
        data = self.cleaned_data.get("character_width")

        if data > 100 or data < -100:
            raise forms.ValidationError("Pick a value between -100 and 100")

        return data

    def clean_line_height(self):
        data = self.cleaned_data.get("line_height")

        if data > 100 or data < -100:
            raise forms.ValidationError("Pick a value between -100 and 100")

        return data

    def clean_symbols(self):
        data = self.data.get("symbols")
        symbol_length = len(data)

        if symbol_length > 100:
            raise forms.ValidationError("Please enter a maximum of 100 characters")

        if symbol_length < 2:
            raise forms.ValidationError("Please enter a minimum of 2 characters")

        return data

class BannerGeneratorForm(forms.Form):
    text = forms.CharField()
    width = forms.IntegerField()

    def clean_text(self):
        data = self.cleaned_data.get("text")

        if len(data) > 60:
            raise forms.ValidationError("Pick a value below 60")

        return data

    def clean_width(self):
        data = self.cleaned_data.get("width")

        if data > 1000 or data < 4:
            raise forms.ValidationError("Pick a value between 8 and 800")

        return data
