from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown as md
register = template.Library()
register = template.Library()
@register.filter()
@stringfilter
def markdown(value):
    return mark_safe(md.markdown(value, extensions=['markdown.extensions.fenced_code']))