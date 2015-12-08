from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'hash', views.hash, name='hash'),
    url(r'gost', views.gost, name='gost'),
    url(r'rsa', views.rsa, name='rsa'),
    url(r'des', views.des, name='des'),
    url(r'sign', views.sign, name='sign'),
]
