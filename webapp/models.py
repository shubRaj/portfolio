from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone, text
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                               related_name="article", related_query_name="has_article", null=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True, blank=True, unique=True)
    published_on = models.DateTimeField(editable=False, default=timezone.now)
    updated_on = models.DateTimeField(editable=False, null=True)
    is_draft = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('app_webapp:article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.title)
        if self.id:
            self.updated_on = timezone.now()
        else:
            self.updated_on = self.published_on
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-published_on", "-updated_on")


class Page(models.Model):
    name = models.CharField(max_length=30, unique=True)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    published_on = models.DateTimeField(editable=False, default=timezone.now)
    updated_on = models.DateTimeField(editable=False, null=True)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.title)
        if self.id:
            self.updated_on = timezone.now()
        else:
            self.updated_on = self.published_on
        super().save(*args, **kwargs)
    # def get_absolute_url(self):
    #     return reverse("app_webapp:pag")


class Configuration(models.Model):
    position = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    about = models.TextField(null=True)
    description = models.CharField(null=True, max_length=50)
    profile = models.ImageField(upload_to="profile")
    large_profile = models.ImageField(upload_to="large_profile", null=True)
    favicon = models.ImageField(upload_to="favicon", null=True)

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name_plural = "Configuration"
