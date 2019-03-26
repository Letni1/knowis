from django.urls import re_path
from ..questions.api import views


app_name = 'api'

urlpatterns = [
    re_path(r'^questions/(?P<slug>.+)/$',
            view=views.QuestionListAPIViewBySlug.as_view(),
            name='questions_by_slug'
            ),
    re_path(r'^questions/$', view=views.QuestionListCreateAPIView.as_view(),
            name='questions_rest_api'),
    # re_path(r'^questions/$', view=views.QuestionListAPIViewByMult.as_view(),
    #         name='questions_filter_api'),
    re_path(r'^questions/u/(?P<username>.+)/$',
            view=views.QuestionListAPIViewByUser.as_view(),
            name='questions_by_user'
            ),
    re_path(r'^questions/d/(?P<uuid>[-\w]+)/$',
            view=views.UserQuestionGetUpdateDeleteByUUID.as_view(),
            name='questions_delete'),
    # re_path(r'^myquestions/$',
    #         view=views.QuestionListAPIViewByMult.as_view(),
    #         name='questions_by_user'),
]
