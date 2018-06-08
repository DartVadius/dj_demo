from django.contrib import admin
from .models import Gallery, Page, Post, Photo
from .forms import GalleryForm


# class GalleryAdmin(admin.ModelAdmin):
#     form = GalleryForm
#
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'description', form.file,),
#         }),
#     )

class ItemAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "screen": ("css/bootstrap/bootstrap.min.css",)
        }
        js = ("js/bootstrap/bootstrap.min.js",)


# admin.site.register(Gallery, ItemAdmin)
admin.site.register(Post, ItemAdmin)
# admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Page, ItemAdmin)
# admin.site.register(Photo)
