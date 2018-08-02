from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="index"),
    url(r'^register$', views.UserFormView.as_view(), name="register"),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^imageUpload', views.imageUpload, name="imageUpload"),
    url(r'^imageView', views.imageView, name="imageView"),
    url(r'^trainModel', views.trainView, name="trainModel"),
    url(r'^save-weights-liver', views.saveWeightLiver, name="saveWeight"),
    url(r'^save-weights-bc', views.saveWeightBc, name="saveWeight"),
    url(r'^check-for-liver', views.checkForLiver, name="checkForLiver"),
    url(r'^check-for-breast-cancer', views.checkForBreastCancer, name="checkForBreastCancer")
]
