from django.urls import re_path
from knowis.questions.api import views



app_name = 'api'

urlpatterns = [
    re_path(r'^question/$', view=views.QuestionListCreatedApiView.as_view(),
            name='questions_rest_api'),
    re_path(r'^question/(?P<uuid>[-\w]+)/$',
            view=views.QuestionRetrieveDestroyAPIView.as_view(),
            name='question_rest_api'
            ),
    re_path(r'^comment/$', view=views.QuestionCommentListCreateAPIView.as_view(),
            name='questions_rest_api'),
    re_path(r'^comment/(?P<uuid>[-\w]+)/$',
            view=views.QuestionCommentDestroyAPIView.as_view(),
            name='question_rest_api'
            ),
]
