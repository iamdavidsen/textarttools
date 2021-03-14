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
            symbols = upload_form.cleaned_data["symbols"]

            color = upload_form.cleaned_data["color"]
            background = upload_form.cleaned_data["background"]

            string = convert_to_text(img, w, sw, sh, symbols)
            return render(request, "image-result.html", {'result': string, 'color': color, 'background': background})
    else:
        upload_form = ImageToAsciiForm(initial={"width": "200", "character_width": 7.7, "line_height" : 18, "symbols": "@=- ", "color": "#33ff33", "background": "#000000"})

    return render(request, "image-to-ascii.html", {'form': upload_form})


def banner_generator_view(request):
    if request.method == "POST":
        upload_form = BannerGeneratorForm(request.POST, request.FILES)

        if upload_form.is_valid():
            text = upload_form.cleaned_data["text"]
            width = upload_form.cleaned_data["width"]

            color = upload_form.cleaned_data["color"]
            background = upload_form.cleaned_data["background"]

            banners = convert_to_banner(text, width)
            return render(request, "banner-result.html", {'result': banners, 'color': color, 'background': background})
    else:
        upload_form = BannerGeneratorForm(initial={"color": "#33ff33", "background": "#000000"})

    return render(request, "banner-generator.html", {'form': upload_form})

def banner_generator_result_view(request, text, page):
    pass


