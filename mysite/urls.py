from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^index', views.post_list, name='post_list'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^', views.post_list, name='post_list'),
]