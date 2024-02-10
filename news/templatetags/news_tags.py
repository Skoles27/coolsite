from django import template
from news.models import *
from news.forms import ContactForm

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag("news/form.html")
def contact_form():
    return {"contact_form": ContactForm()}
