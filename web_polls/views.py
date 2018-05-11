from django.http import HttpResponse
from web_polls.models import Question


# A view in Django is a function or amethon in case of class-based views
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    """detail view of the web_poll application"""
    response = "You're looking at question %s details." % question_id
    return HttpResponse(response)


def results(request, question_id):
    """results view of the web_poll application"""
    response = "You're looking at question %s results." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    """vote view of the web_poll application"""
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
