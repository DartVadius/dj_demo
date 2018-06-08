from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Gallery(models.Model):
    name = models.CharField(max_length=255, null=False)
    slug = models.CharField(max_length=255, null=True, unique=True, blank=True)
    # description = HTMLField()
    description = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=45, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(
        default=timezone.now)
    date_update = models.DateTimeField(
        blank=True, null=True)

    def update(self):
        self.date_update = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    slug = models.CharField(max_length=255, unique=True, null=False)
    text = HTMLField()
    meta_title = models.CharField(max_length=45, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(
        default=timezone.now)
    date_update = models.DateTimeField(
        blank=True, null=True)

    def update(self):
        self.date_update = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Photo(models.Model):
    path = models.CharField(max_length=255, unique=True, null=False)
    description = models.CharField(max_length=255, unique=False, null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    # image = models.ImageField(upload_to='photos/',)

    def __str__(self):
        return self.path


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False)
    slug = models.CharField(max_length=255, unique=True, null=False)
    short_text = models.TextField(max_length=255)
    # text = models.TextField()
    text = HTMLField()
    meta_title = models.CharField(max_length=45, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(
        default=timezone.now)
    date_update = models.DateTimeField(
        blank=True, null=True)

    def update(self):
        self.date_update = timezone.now()
        self.save()

    def __str__(self):
        return self.title
