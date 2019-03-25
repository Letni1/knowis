from django.urls import re_path
from ..questions.api import views


app_name = 'api'

urlpatterns = [
    re_path(r'^questions/$', view=views.QuestionListCreateAPIView.as_view(),
            name='questions_rest_api'),
    re_path(r'^questions/u/(?P<username>.+)/$',
            view=views.QuestionListAPIViewByUser.as_view(),
            name='question_rest_api'
            ),
    re_path(r'^questions/(?P<slug>.+)/$',
            view=views.QuestionRetrieveUpdateDestroyBySlug.as_view(),
            name='question_rest_api'
            ),
    re_path(r'^myquestions/$',
            view=views.QuestionListAPIViewByMult.as_view(),
            name='question_rest_api')
]
