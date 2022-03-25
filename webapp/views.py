from audioop import reverse
from django.views import generic
from .models import Article, Page
from django.shortcuts import render
from django.template.defaultfilters import timesince
from django.contrib.auth import get_user_model
from django.db.models.functions import ExtractYear
import datetime

class HomeView(generic.ListView):
    template_name = "webapp/home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(is_draft=False)[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles_count"] = Article.objects.filter(
            is_draft=False).count()
        return context


class ArticleView(generic.DetailView):
    template_name = "webapp/detail.html"
    context_object_name = "article"
    model = Article


class PageDetailView(generic.DetailView):
    template_name = "webapp/page_detail.html"
    context_object_name = "page"
    model = Page


class ArticleYearView(generic.View):
    template_name = "webapp/blogs.html"
    context_object_name = "articles"
    model = Article
    def get_queryset(self):
        return self.model.objects.filter(is_draft=False)
    def get(self, request, *args, **kwargs):
        context = {}
        USER = get_user_model()
        superuser = USER.objects.filter(
            is_superuser=True).order_by("date_joined")
        if superuser.exists():
            since = superuser.first().date_joined.date()
            today = datetime.date.today()
            timedelta_escaped = (today - since)
            days = timedelta_escaped.days
            if days > 365:
                years = days//365
                since = f"{years}{'year' if years>1 else 'years'}"
            elif days > 30:
                months = days//30
                since = f"{months}{'month' if months>1 else 'months'}"
            elif days < 1:
                since = timesince(since)
            elif days < 2:
                since = f"{round(days * 24)} hours"
            else:
                since = f"{days} days"
            context["since"] = since
        qs = self.get_queryset().annotate(year=ExtractYear(
            "published_on")).order_by("-published_on")
        if qs.exists():
            years = set(qs.order_by("-year").values_list("year", flat=True))
            results = [{"year": year, "objects": qs.filter(
                year=year)} for year in years]
            context.update({self.context_object_name: results,
                           "posts_count": qs.count(), })
        return render(request, self.template_name, context)

