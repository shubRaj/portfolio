from django.views import generic
from .models import Article
from django.shortcuts import render
from django.db.models.functions import ExtractYear


class HomeView(generic.ListView):
    template_name = "webapp/home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles_count"] = Article.objects.count()
        return context


class ArticleView(generic.DetailView):
    template_name = "webapp/detail.html"
    context_object_name = "article"
    model = Article


class ArticleYearView(generic.View):
    template_name = "webapp/blogs.html"
    context_object_name = "articles"
    model = Article

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.annotate(year=ExtractYear(
            "published_on")).order_by("-published_on")
        if qs.exists():
            years = set(qs.order_by("-year").values_list("year", flat=True))
            results = [{"year": year, "objects": qs.filter(
                year=year)} for year in years]
            return render(request, self.template_name, {self.context_object_name: results, "posts_count": qs.count(), "oldest_post": qs.last().published_on})
        return render(request,self.template_name)
