from django.urls import path

from asciitools.views import home_view, image_to_ascii_view, banner_generator_view

urlpatterns = [
    path('', home_view, name="home"),
    path('image-to-ascii', image_to_ascii_view, name="image_to_ascii"),
    path('ascii-text-banner-generator', banner_generator_view, name="text_to_banner"),
]
