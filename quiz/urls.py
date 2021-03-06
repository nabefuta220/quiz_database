from django.urls import path

from . import views

urlpatterns = [
    # /quiz/
    path('', views.index, name='index'),
    # /quiz/list/
    path('list/', views.list, name='question list'),
    # /puiz/list/[number]/
    path('list/<int:question_id>', views.detail, name='detail'),
    # /quiz/tag/
    path('tag/', views.taglist, name='taglist'),
    # /quiz/tag/[tagname]/
    path('tag/tree/<str:tagname>', views.tagtree, name='tag'),
    # /quiz/tag/lists/[tagname]/
    path('tag/lists/<str:tagname>', views.tag_include, name='lists'),
    # /quiz/next/tag=[tagname],round=[round]/
    path('answer/next/tag=<str:tagname>,round=<int:round>',
         views.Quiz_check, name='next'),
    # /quiz/question/tag=[tagname],round=[round]
    path('form/check/tag=<str:tagname>,round=<int:round>',
         views.serve_problem, name='check'),
]
