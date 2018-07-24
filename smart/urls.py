from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="index"),
    url(r'^imageUpload', views.imageUpload, name="imageUpload"),
    url(r'^imageView', views.imageView, name="imageView"),
    url(r'^trainModel', views.trainView, name="trainModel"),
    url(r'^save-weights', views.saveWeight, name="saveWeight")
]
