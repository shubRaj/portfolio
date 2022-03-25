from django.contrib.sitemaps import Sitemap
from .models import Article, Page

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    protocol = "https"
    limit = 100
    def items(self):
        return Article.objects.filter(is_draft=False)
    def lastmod(self, obj):
        return obj.updated_on
class PageSitemap(BlogSitemap):
    def items(self):
        return Page.objects.filter(is_draft=False)