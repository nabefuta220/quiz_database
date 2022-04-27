
import queue
from django.db.models import Q
from django.http import  HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render



from .models import Question,Tag

# Create your views here.


def index(request):
    return HttpResponse("hello")


def list(request):
    q = get_list_or_404(Question)
    context={'question_list': q}
    return render(request,'quiz/detail.html',context)


def detail(request, question_id: int):
    q = get_list_or_404(Question,id=question_id)
    context={'question_list': q}
    return render(request,'quiz/detail.html',context)


def taglist(request):

    
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'quiz/taglist.html', context)


def tagtree(request,tagname:str):

    target = get_object_or_404(Tag, name=tagname)
    child_list = target.child_tag.all()
    context = {'target_tag': tagname,'child':child_list,'parament':target.parament_tag}
    return render(request, 'quiz/tagtree.html', context)

def tag_include(request,tagname):
    
    tag=Tag.objects.get(name=tagname)
    query=tag_include_sub(tag)
    
    
    problems = get_list_or_404(Question, query)
    context = {'question_list': problems}
    return render(request, 'quiz/detail.html', context)

def tag_include_sub(tagname:Tag):
    query = Q(tag=tagname)
    child=tagname.child_tag.all()
    for tags in child:
        query|= tag_include_sub(tags)
    return query