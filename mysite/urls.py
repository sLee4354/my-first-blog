from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', views.post_list, name='post_list'),
    url(r'^index/', views.indexPage, name='indexPage'),
]