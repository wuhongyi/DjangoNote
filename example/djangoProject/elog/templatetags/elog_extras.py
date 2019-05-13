from django import template

register = template.Library()

@register.filter
def div(value, arg):
    if float(arg) == 0 or arg is None:
        return 0

    return float(value)/float(arg)
