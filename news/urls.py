from django.urls import  path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60 * 15)(Home.as_view()), name='home'),
    path('news_posts/', cache_page(60 * 15)(NewsPostsList.as_view()), name='news_posts'),
    path('legal_cases/', cache_page(60 * 15)(LegalCasesPostsList.as_view()), name='legal_cases'),
    path('social_work/', cache_page(60 * 15)(SocialWorkPostsList.as_view()), name='social_work'),
    path('education/', cache_page(60 * 15)(EducationPostsList.as_view()), name='education'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('category/<slug:cat_slug>/', NewsCategory.as_view(), name='category'),
    path('search/', SearchNews.as_view(), name='search'),
    path('post/<slug:post_slug>/', ShowNewsPost.as_view(), name='post'),
    path('legal_cases_post/<slug:legal_cases_post_slug>/', ShowLegalCasePost.as_view(), name='legal_cases_post'),
    path('social_work_post/<slug:social_work_post_slug>/', ShowSocialWorkPost.as_view(), name='social_work_post'),
    path('education_post/<slug:education_post_slug>/', ShowEducationPost.as_view(), name='education_post'),
]
