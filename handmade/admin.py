from django.contrib import admin
from .models import Gallery, Page, Post, Photo
from .forms import GalleryForm


class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'file',),
        }),
    )


admin.site.register(Post)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Page)
admin.site.register(Photo)






