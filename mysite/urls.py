from django.conf.urls import include, url
from django.contrib import admin
from api.resources import NoteResource
from . import views
note_resource = NoteResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(note_resource.urls)),
    #url(r'^index', views.post_list, name='post_list'),
    #url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^', include('blog.url')),
]