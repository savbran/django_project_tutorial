from django.http import HttpResponse
from web_polls.models import Question
from django.shortcuts import render
from django.shortcuts import get_object_or_404


# A view in Django is a function or amethon in case of class-based views
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, latest_question_list, context)


def detail(request, question_id):
    """detail view of the web_poll application"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'web_polls/detail.html', {'question': question})


def results(request, question_id):
    """results view of the web_poll application"""
    response = "You're looking at question %s results." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    """vote view of the web_poll application"""
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
