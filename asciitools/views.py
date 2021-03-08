from django.shortcuts import render
from PIL import Image, ImageOps

from asciitools.converters import convert_to_text
from asciitools.forms import ImageToAsciiForm


def home_view(request):
    return render(request, "home.html", {})


def image_to_ascii_view(request):
    if request.method == "POST":
        upload_form = ImageToAsciiForm(request.POST, request.FILES)

        if upload_form.is_valid():
            img = ImageOps.exif_transpose(Image.open(upload_form.cleaned_data["image"]))
            w = upload_form.cleaned_data["width"]
            sw = upload_form.cleaned_data["character_width"]
            sh = upload_form.cleaned_data["line_height"]


            string = convert_to_text(img, w, sw, sh)
            return render(request, "image-result.html", { 'result': string })
    else:
        upload_form = ImageToAsciiForm()

    return render(request, "image-to-ascii.html", {'form': upload_form})
