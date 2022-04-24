from django.urls import path

from . import views

urlpatterns = [
    # /quiz/
 path('', views.index, name='index'),
    # /quiz/list/
    path('list/',views.list,name='question list'),
    # /puiz/list/[number]/
    path('list/<int:question_id>',views.detail,name='detail'),
]
