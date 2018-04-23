from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.post_list, name='post_list'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
]