from django.core.cache import cache
from django.db.models import Count

from .models import *

menu = [{'title': "Правовые дела", 'url_name': 'legal_cases'},
        {'title': "Общественная деятельность", 'url_name': 'social_work'},
        {'title': "Образование", 'url_name': 'education'},
        {'title': "Обратная связь", 'url_name': 'contact'}]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('news'))
            cache.set('cats', cats, 60)

        user_menu = menu.copy()
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
