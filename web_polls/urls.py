'''
Created on 07 mag 2018

@author: saverio
'''
from django.urls.conf import path

from . import views

app_name = 'web_polls'
# urlconf
urlpatterns = [
    # url patterns
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='votes'),
]
