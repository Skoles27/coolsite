from itertools import chain

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import context, RequestContext
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView

# Create your views here.
from .forms import *
from .models import *
from .utils import *


class Home(DataMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('cat')


class NewsPostsList(DataMixin, ListView):
    paginate_by = 7
    model = News
    template_name = 'news/news_posts.html'
    context_object_name = 'news_posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsPostsList, self).get_context_data(**kwargs)
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title="Все новости")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('cat')


class ShowNewsPost(DataMixin, DetailView):
    model = News
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowNewsPost, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class NewsCategory(DataMixin, ListView):
    paginate_by = 7
    model = News
    template_name = 'news/news_posts.html'
    context_object_name = 'news_posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsCategory, self).get_context_data(**kwargs)
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ContactFormView(DataMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'news/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))


class LegalCasesPostsList(DataMixin, ListView):
    paginate_by = 7
    model = LegalCases
    template_name = 'news/legal_cases.html'
    context_object_name = 'legal_cases_posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LegalCasesPostsList, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title="Правовые дела")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return LegalCases.objects.filter(is_published=True)


class ShowLegalCasePost(DataMixin, DetailView):
    model = LegalCases
    template_name = 'news/legal_cases_post.html'
    slug_url_kwarg = 'legal_cases_post_slug'
    context_object_name = 'legal_cases_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowLegalCasePost, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title=context['legal_cases_post'])
        return dict(list(context.items()) + list(c_def.items()))


class SocialWorkPostsList(DataMixin, ListView):
    paginate_by = 7
    model = SocialWork
    template_name = 'news/social_work.html'
    context_object_name = 'social_work_posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SocialWorkPostsList, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title="Общественная деятельность")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return SocialWork.objects.filter(is_published=True)


class ShowSocialWorkPost(DataMixin, DetailView):
    model = SocialWork
    template_name = 'news/social_work_post.html'
    slug_url_kwarg = 'social_work_post_slug'
    context_object_name = 'social_work_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowSocialWorkPost, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['education'] = Education.objects.all()
        c_def = self.get_user_context(title=context['social_work_post'])
        return dict(list(context.items()) + list(c_def.items()))


class EducationPostsList(DataMixin, ListView):
    paginate_by = 7
    model = Education
    template_name = 'news/education.html'
    context_object_name = 'education_posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EducationPostsList, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        c_def = self.get_user_context(title="Образование")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Education.objects.filter(is_published=True)


class ShowEducationPost(DataMixin, DetailView):
    model = Education
    template_name = 'news/education_post.html'
    slug_url_kwarg = 'education_post_slug'
    context_object_name = 'education_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowEducationPost, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        c_def = self.get_user_context(title=context['education_post'])
        return dict(list(context.items()) + list(c_def.items()))


class SearchNews(DataMixin, ListView):
    template_name = 'news/search.html'
    context_object_name = 'search'

    def get_queryset(self):
        objects_list = [News, LegalCases, SocialWork, Education]
        search_list = []
        for o in objects_list:
            search_list += o.objects.filter(title__icontains=self.request.GET.get("q"))
        return search_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchNews, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['legalcases'] = LegalCases.objects.all()
        context['socialwork'] = SocialWork.objects.all()
        context['education'] = Education.objects.all()
        context["q"] = self.request.GET.get("q")
        c_def = self.get_user_context(title="Результаты поиска")
        return dict(list(context.items()) + list(c_def.items()))
