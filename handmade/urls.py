from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gallery_list, name='gallery_list'),
]