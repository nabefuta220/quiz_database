
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from .models import Question, Tag

# Create your views here.


def index(request):
    """
    タイトル画面を表示する
    """
    return render(request, 'quiz/jikken5-1html.html', None)


def list(request):
    """
    問題リストを表示する
    """
    q = get_list_or_404(Question)
    context={'question_list': q,'message':'問題一覧','tag':'all'}
    return render(request,'quiz/detail.html',context)


def detail(request, question_id: int):
    """
    該当する問題の詳細を表示する
    """
    q = get_list_or_404(Question,id=question_id)
    context = {'question_list': q, 'message': '問題詳細'}
    return render(request,'quiz/detail.html',context)


def taglist(request):
    """
    タグの一覧を表示する
    """
    
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'quiz/taglist.html', context)


def tagtree(request,tagname:str):
    """
    タグに属するタグを表示する
    """
    target = get_object_or_404(Tag, name=tagname)
    child_list = target.child_tag.all()
    context = {'target_tag': tagname,'child':child_list,'parament':target.parament_tag}
    return render(request, 'quiz/tagtree.html', context)


def tag_include(request,tagname:str):
    """
    タグに属する問題を表示する
    """
    tag=Tag.objects.get(name=tagname)
    query=tag_include_sub(tag)
    
    problems = get_list_or_404(Question, query)
    context = {'question_list': problems, 'message':f'{tagname}に属する問題一覧','tag':tagname}
    return render(request, 'quiz/detail.html', context)

def tag_include_sub(tagname:Tag):
    query = Q(tag=tagname)
    child=tagname.child_tag.all()
    for tags in child:
        query|= tag_include_sub(tags)
    return query

def Quiz_check(request, tagname:str,round:int):
    """
    解答判定画面を表示する
    """
    #ボタンが押されたときの処理
    if request.method == "POST":
        print("poseted")
        if "next_button" in request.POST:
            return redirect("question",tagname,round+1)
            
        elif "exit_button" in request.POST:
            return redirect("index")

        if "next_button" in request.POST:
            answer = request.POST["enter"]
    if tagname == 'all':
        question = Question.objects.all()[round]
    else:
        tag = Tag.objects.get(name=tagname)
        query=tag_include_sub(tag)
        question=Question.objects.filter(query)[round]
    print(question)
    correct_answer=question.answer_text

    context = {'answer':correct_answer is answer,'tagname':tagname,'round':round}
    return render(request, 'quiz/quiz_result.html', context)


def serve_problem(request,tagname:str,round:int):
    """
    問題を出題する
    (すべての問題を出題し終わったときは終了画面を出す)
    """
    try:
        if tagname == 'all':
            question=Question.objects.all()[round]
        else:
            tag = Tag.objects.get(name=tagname)
            query = tag_include_sub(tag)
            question = Question.objects.filter(query)[round]
    except IndexError:
        #終了画面を出す
        return render(request, 'quiz/end.html', None)
    else:
        print('next:')
        print(question)
        #問題を出題する
        return render(request,'hoge.html',{'problem':question, "tagname":tagname, "round":round})
