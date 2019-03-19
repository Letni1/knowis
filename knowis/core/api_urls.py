from django.urls import re_path
from ..questions.api import views



app_name = 'api'

urlpatterns = [
    re_path(r'^questions/$', view=views.QuestionGetList.as_view(),
            name='questions_rest_api'),
#     re_path(r'^comments/$', view=views.QuestionCommentListCreateAPIView.as_view(),
#             name='questions_rest_api'),
#     re_path(r'^comments/(?P<uuid>[-\w]+)/$',
#             view=views.QuestionCommentDestroyAPIView.as_view(),
#             name='question_rest_api'
#             ),
    re_path(r'^questions/(?P<slug>[-\w]+)/$',
            view=views.QuestionListBySlug.as_view(),
            name='question_rest_api'
            ),
    re_path(r'^myquestions/$', view=views.UserQuestionGetList.as_view(),
            name='question_rest_api'),
    re_path(r'^myquestions/(?P<uuid>[-\w]+)/$',
            view=views.UserQuestionListDeleteByUUID.as_view(),
            name='question_rest_api'
            ),
]
