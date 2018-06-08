from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from handmade.views import show_admin_gallery_list, add_gallery, update_gallery, add_photo, update_photo, delete_photo

urlpatterns = [
    # url(r'^$', views.gallery_list, name='gallery_list'),
    url(r'^admin/admin-gallery-list/$', user_passes_test(lambda u: u.is_superuser)(show_admin_gallery_list),
        name='admin_gallery'),
    url(r'^admin/admin-gallery-add/$', user_passes_test(lambda u: u.is_superuser)(add_gallery),
        name='admin_gallery_add'),
    url(r'^tinymce/', include('tinymce.urls')),
    path('admin/admin-gallery-update/<int:gallery_id>/', user_passes_test(lambda u: u.is_superuser)(update_gallery),
         name='admin_gallery_update'),
    path('admin/add-photo/<int:gallery_id>/', user_passes_test(lambda u: u.is_superuser)(add_photo),
         name='add_photo'),
    path('admin/update-photo/<int:photo_id>/', user_passes_test(lambda u: u.is_superuser)(update_photo),
         name='update_photo'),
    path('admin/delete-photo/<int:photo_id>/', user_passes_test(lambda u: u.is_superuser)(delete_photo),
         name='delete_photo'),
]
