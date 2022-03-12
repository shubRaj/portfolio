from django.urls import path
from .views import ArticleYearView, HomeView, ArticleView
from django.views import generic
app_name = "app_webapp"
urlpatterns = [
    path("blog/<slug:slug>/", ArticleView.as_view(), name="article_detail"),
    path("about/", generic.TemplateView.as_view(template_name="webapp/about.html"), name="about"),
    path("blogs/", ArticleYearView.as_view(), name="articles"),
    path("", HomeView.as_view(), name="home"),
]
