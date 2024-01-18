# custom_filters.py

from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.filter(name='highlight')
def highlight(text, query):
    highlighted_text = text.replace(query, f'<span style="background-color: yellow;">{query}</span>')
    return mark_safe(highlighted_text)