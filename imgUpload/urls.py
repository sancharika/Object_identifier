from django.contrib import admin
from django.conf.urls import url
from django.urls.conf import include
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'imageprocess',views.imageprocess,name="imageprocess")
]
