from django.shortcuts import render
from handmade.models import Gallery, Photo
from django.http import HttpResponseRedirect
from handmade.forms import GalleryForm, GalleryFormUpdate, PhotoForm, PhotoUpdateForm
from slugify import slugify
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from PIL import Image, ImageFilter
import time
import os


def gallery_list(request):
    return render(request, 'handmade/gallery_list.html', {})


def show_admin_gallery_list(request):
    galleries_list = Gallery.objects.all()
    paginator = Paginator(galleries_list, 5)
    page = request.GET.get('page')
    galleries = paginator.get_page(page)
    ctx = {'data': galleries}
    return render(request, 'handmade/admin_gallery_list.html', ctx)


def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        # form.fields['id'].widget = HiddenInput()
        if form.data['slug']:
            form.fields['slug'].initial = slugify(form.data['slug'])
        else:
            form.fields['slug'].initial = slugify(form.data['name'])
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.save()
            return HttpResponseRedirect('/admin/admin-gallery-list/')
    else:
        form = GalleryForm()
    return render(request, 'handmade/add_gallery.html', {'form': form})


def update_gallery(request, gallery_id):
    if request.method == 'POST':
        form = GalleryFormUpdate(request.POST)
        del form.errors['slug']
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.id = gallery_id
            gallery.date_create = Gallery.objects.get(pk=gallery_id).date_create
            if hasattr(gallery, 'slug'):
                gallery.slug = slugify(gallery.slug)
            else:
                gallery.slug = slugify(gallery.name)
            gallery.update()
            return HttpResponseRedirect('/admin/admin-gallery-list/')
    else:
        gallery = Gallery.objects.get(pk=gallery_id)
        form = GalleryFormUpdate(instance=gallery)

    return render(request, 'handmade/add_gallery.html', {'form': form})


def add_photo(request, gallery_id):
    if request.method == 'POST':
        if request.FILES['image']:
            for file in request.FILES.getlist('image'):
                fs = FileSystemStorage()
                filename = fs.save(str(gallery_id) + '/' + str(round(time.time())) + '_' + file.name, file)
                splited = filename.split('/')
                splited[-1] = 'thumb_' + splited[-1]
                thumb_path = '/'.join(splited)
                uploaded_file_url = fs.url(filename)
                img = Photo()
                img.gallery_id = gallery_id
                img.path = uploaded_file_url
                img.save()
                img = Image.open('media/' + filename)
                size = (280, 280)
                img.thumbnail(size)
                img.save('media/' + thumb_path)
        return HttpResponseRedirect('/admin/admin-gallery-list/')
    else:
        photos = Photo.objects.filter(gallery_id=gallery_id)
        for photo in photos:
            path = photo.path
            splited = path.split('/')
            splited[-1] = 'thumb_' + splited[-1]
            photo.path = '/'.join(splited)
        form = PhotoForm()
        photo_update_form = PhotoUpdateForm()
    return render(request, 'handmade/add_photo.html',
                  {'form': form, 'photo_update_form': photo_update_form, 'photos': photos})


def update_photo(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        photo.description = request.POST['photo_desc']
        photo.save()
        form = PhotoForm()
        photo_update_form = PhotoUpdateForm()
        photos = Photo.objects.filter(gallery_id=photo.gallery_id)
        return render(request, 'handmade/add_photo.html',
                      {'form': form, 'photo_update_form': photo_update_form, 'photos': photos})
    return HttpResponseRedirect('/admin/admin-gallery-list/')


def delete_photo(request, photo_id):
    if request.method == 'GET':
        photo = Photo.objects.get(pk=photo_id)
        gallery_id = photo.gallery_id
        photo.delete()
        url = reverse('add_photo', kwargs={'gallery_id': gallery_id})
        return HttpResponseRedirect(url)
    return HttpResponseRedirect('/admin/admin-gallery-list/')
