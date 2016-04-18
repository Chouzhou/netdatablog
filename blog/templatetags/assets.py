from django import template
from netdatablog.settings import IS_DEVELOP

register = template.Library()


@register.filter
def assets(value):
    if IS_DEVELOP:
        return "/static/assets/" + value
    value = "/static/" + value
    # value.upper()
    return value
