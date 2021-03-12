from django.urls import path
from django.views.generic.base import TemplateView

from asciitools.views import image_to_ascii_view, banner_generator_view

urlpatterns = [
    path('', image_to_ascii_view, name="image_to_ascii"),
    path('ascii-text-banner-generator', banner_generator_view, name="text_to_banner"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
