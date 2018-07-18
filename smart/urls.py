from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imageUpload', views.imageUpload, name="imageUpload"),
    url(r'^imageView', views.imageView, name="imageView"),
]
