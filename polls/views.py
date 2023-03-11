from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question

# Create your views here.


def index(request):
    content_ordered_by_latest = Question.objects.order_by("-pub_date")[:5]
    return render(
        request, "polls/index.html", {"latest_polls": content_ordered_by_latest}
    )


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
