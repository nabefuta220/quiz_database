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
]
