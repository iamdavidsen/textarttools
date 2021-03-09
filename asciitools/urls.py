from django.urls import path

from asciitools.views import image_to_ascii_view, banner_generator_view

urlpatterns = [
    path('', image_to_ascii_view, name="image_to_ascii"),
    path('ascii-text-banner-generator', banner_generator_view, name="text_to_banner"),
]
