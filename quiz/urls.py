from django.urls import path

from . import views

urlpatterns = [
    # /quiz/
    path('', views.index, name='index'),
    # /quiz/list/
    path('list/',views.list,name='question list'),
    # /puiz/list/[number]/
    path('list/<int:question_id>',views.detail,name='detail'),
    #/quiz/tag/
    path('tag/', views.taglist, name='taglist'),
    #/quiz/tag/[tagname]/
    path('tag/tree/<str:tagname>',views.tagtree,name='tag'),
    #/quiz/tag/lists/[tagname]/
    path('tag/lists/<str:tagname>', views.tag_include, name='lists'),
    path('answer/next/answer=<str:answer>,id=<int:number>', views.Quiz_check, name='next'),
    # path('answer/next/answer=<str:answer>,tag=<str:tagneme>,round=<int:round>', views.Quiz_check, name='next'),
    path('answer/title/', views.Quiz_check, name='title'),
]
