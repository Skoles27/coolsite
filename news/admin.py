from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms

from .models import *


# Register your models here.

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class LegalCasesAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class SocialWorkAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class EducationAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    form = NewsAdminForm


class LegalCasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    form = LegalCasesAdminForm


class SocialWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    form = SocialWorkAdminForm


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    form = EducationAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "content", "date")


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(LegalCases, LegalCasesAdmin)
admin.site.register(SocialWork, SocialWorkAdmin)
admin.site.register(Education, EducationAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель сайта'
