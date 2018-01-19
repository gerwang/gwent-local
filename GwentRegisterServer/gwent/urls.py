from django.conf.urls import url

from . import views

app_name = 'gwent'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^ranklist/$', views.ranklist, name='ranklist'),
    url(r'^handle/$', views.handle, name='handle'),
]
