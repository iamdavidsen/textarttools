from django.shortcuts import render
from PIL import Image, ImageOps

from asciitools.converters import convert_to_text, convert_to_banner
from asciitools.forms import ImageToAsciiForm, BannerGeneratorForm


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
            return render(request, "image-result.html", {'result': string})
    else:
        upload_form = ImageToAsciiForm()

    return render(request, "image-to-ascii.html", {'form': upload_form})


def banner_generator_view(request):
    if request.method == "POST":
        upload_form = BannerGeneratorForm(request.POST, request.FILES)

        if upload_form.is_valid():
            text = upload_form.cleaned_data["text"]

            banners = convert_to_banner(text)
            return render(request, "banner-generator.html", {'from': upload_form, 'result': banners})
    else:
        upload_form = BannerGeneratorForm()

    return render(request, "banner-generator.html", {'form': upload_form})
