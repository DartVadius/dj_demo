from django import forms
from handmade.my_forms.form_fields import SlugUpdateField
from .models import Gallery, Photo
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django.contrib import admin


class GalleryForm(forms.ModelForm):
    # description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Gallery
        fields = ('name', 'slug', 'description', 'meta_title', 'meta_description', 'meta_keywords',)
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'meta_description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }


class GalleryFormUpdate(forms.ModelForm):
    # description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    # name = forms.CharField(label='Название галереи', max_length=255, required=True)
    # slug = forms.SlugField(label='Slug', max_length=255, required=False)
    # slug = SlugUpdateField(label='Slug', max_length=255)
    # meta_title = forms.CharField(label='Мета тайтл', max_length=255, required=False)
    # meta_keywords = forms.CharField(label='Ключевые слова', max_length=255, required=False)
    # description = forms.CharField(widget=forms.Textarea, required=True, label='Краткое описание')
    # meta_description = forms.CharField(widget=forms.Textarea, required=False, label='Мета описание')

    # files = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Gallery
        fields = ('name', 'slug', 'description', 'meta_title', 'meta_description', 'meta_keywords',)
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 10}),
            'meta_description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }


class PhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True,
                             label='Фотографии')


class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('description',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }
