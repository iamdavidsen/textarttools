from django.shortcuts import render
from PIL import Image, ImageOps

from asciitools.converters import convert_to_text, convert_to_banner
from asciitools.forms import ImageToAsciiForm, BannerGeneratorForm

def image_to_ascii_view(request):
    if request.method == "POST":
        upload_form = ImageToAsciiForm(request.POST, request.FILES)

        if upload_form.is_valid():
            img = ImageOps.exif_transpose(Image.open(upload_form.cleaned_data["image"]))
            w = upload_form.cleaned_data["width"]
            sw = upload_form.cleaned_data["character_width"]
            sh = upload_form.cleaned_data["line_height"]
            symbols = upload_form.cleaned_data["symbols"]

            string = convert_to_text(img, w, sw, sh, symbols)
            return render(request, "image-result.html", {'result': string})
    else:
        upload_form = ImageToAsciiForm(initial={"width": "200", "character_width": 7.2, "line_height" : 18, "symbols": "@=- "})

    return render(request, "image-to-ascii.html", {'form': upload_form})


def banner_generator_view(request):
    if request.method == "POST":
        upload_form = BannerGeneratorForm(request.POST, request.FILES)

        if upload_form.is_valid():
            text = upload_form.cleaned_data["text"]
            width = upload_form.cleaned_data["width"]

            banners = convert_to_banner(text, width)
            return render(request, "banner-result.html", {'result': banners})
    else:
        upload_form = BannerGeneratorForm()

    return render(request, "banner-generator.html", {'form': upload_form})
