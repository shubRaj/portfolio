from django.urls import path
from .views import ArticleYearView, HomeView, ArticleView, robots_txt,PageDetailView
from django.views import generic
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap
app_name = "app_webapp"
sitemaps = {
    'blogs': BlogSitemap,
}
urlpatterns = [
    path("robots.txt", robots_txt, name="robot"),
    path("blog/<slug:slug>/", ArticleView.as_view(), name="article_detail"),
    path("about/", generic.TemplateView.as_view(template_name="webapp/about.html"), name="about"),
    path("blogs/", ArticleYearView.as_view(), name="articles"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path("<slug:slug>/",PageDetailView.as_view(),name="page_detail"),
    path("", HomeView.as_view(), name="home"),
]
