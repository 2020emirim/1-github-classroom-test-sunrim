from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #  최신날짜 순으로 5개 가져온다~
    output = ', '.join([q.question_text for q in latest_question_list])
    # ["좋아하는 가수?", "좋아하는 색깔?"]
    # "좋아하는 가수?", "좋아하는 색깔?"
    return HttpResponse(output)
    return


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
