from django.http import HttpResponse


# A view in Django is a function or amethon in case of class-based views
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
