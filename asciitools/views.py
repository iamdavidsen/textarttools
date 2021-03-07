from django.shortcuts import render
from PIL import Image

from asciitools.converters import convert_to_text
from asciitools.forms import ImageToAsciiForm


def home_view(request):
    return render(request, "home.html", {})


def image_to_ascii_view(request):
    if request.method == "POST":
        upload_form = ImageToAsciiForm(request.POST, request.FILES)

        if upload_form.is_valid():
            string = convert_to_text(Image.open(upload_form.cleaned_data["image"]))
            return render(request, "image-result.html", { 'result': string })

    return render(request, "image-to-ascii.html", {})

def image_to_emoji_view(request):
    return render(request, "image-to-ascii.html", {})

