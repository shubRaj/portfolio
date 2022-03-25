from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.urls import reverse

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        f"Sitemap: {request.build_absolute_uri(reverse('django.contrib.sitemaps.views.index'))}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")