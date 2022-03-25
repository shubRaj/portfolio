from django.contrib import admin
from .models import Article, Configuration, Page


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "body", "author__username",
                     "author__first_name", "author__last_name")
    date_hierarchy = "published_on"
    list_filter = ("author",)


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position")
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("name","updated_on")
    prepopulated_fields = {"slug": ("name",)}