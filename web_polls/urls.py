'''
Created on 07 mag 2018

@author: saverio
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]