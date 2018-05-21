'''
Created on 18 mag 2018

@author: saverio
'''
from django.urls.conf import path

from . import views

app_name = 'wordcount'
# urlconf
urlpatterns = [
    # url patterns
    path('', views.home, name='home'),
    ]
