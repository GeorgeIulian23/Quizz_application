from django.template.defaulttags import register

# Custom template filter to get data from a dictionary using key in template
from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val