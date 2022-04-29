
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, render


from .models import Question

# Create your views here.


def index(request):
    return render(request, 'quiz/jikken5-1html.html', None)


def list(request):
    q = get_list_or_404(Question)
    context={'question_list': q}
    return render(request,'quiz/detail.html',context)


def detail(request, question_id: int):
    q = get_list_or_404(Question,id=question_id)
    context={'question_list': q}
    return render(request,'quiz/detail.html',context)
