from django.urls import path
from django.views.generic.base import TemplateView

from asciitools.views import image_to_ascii_view, banner_generator_view, home_view, redirect_view

urlpatterns = [
    path('', image_to_ascii_view, name="image_to_ascii"),
    path('ascii-banner', banner_generator_view, name="text_to_banner"),
    path('image-to-ascii', redirect_view, name="old-image-to-ascii"),
]

#path('ascii-banner-generator/<str:text>/<int/page>/', banner_generator_view, name="text_to_banner"),
