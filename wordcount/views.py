from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

    
