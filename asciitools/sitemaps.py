from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['image_to_ascii', 'text_to_banner']

    def location(self, item):
        return reverse(item)
