from django.urls import re_path
from ..questions.api import views as q_views
from ..useraccount.api import views as u_views

app_name = 'api'

urlpatterns = [
    re_path(r'^questions/u/(?P<username>.+)/$',
            view=q_views.QuestionListAPIViewByUser.as_view(),
            name='list_questions_by_username'
            ),
    re_path(r'^questions/d/(?P<slug>.+)/$',
            view=q_views.UserQuestionGetUpdateDeleteBySlug.as_view(),
            name='gud_question_by_slug'),
    # re_path(r'^questions/d/(?P<uuid>[-\w]+)/$',
    #         view=q_views.UserQuestionGetUpdateDeleteByUUID.as_view(),
    #         name='questions_delete'),
    re_path(r'^questions/(?P<slug>.+)/$',
            view=q_views.QuestionListAPIViewBySlug.as_view(),
            name='get_question_by_slug'
            ),
    re_path(r'^question/$',
            view=q_views.QuestionPostAPIView.as_view(),
            name='create_question'
            ),
    re_path(r'^questions/$', view=q_views.QuestionListAPIView.as_view(),
            name='list_published_questions'),
    # re_path(r'^questions/$', view=views.QuestionListAPIViewByMult.as_view(),
    #         name='questions_filter_api'),
    re_path(r'^answers/d/(?P<uuid>[-\w]+)/$',
            view=q_views.AnswerGetUpdateDeleteByUUID.as_view(),
            name='questions_delete'),
    re_path(r'^answers/q/(?P<uuid>[-\w]+)/$',
            view=q_views.AnswersListApiViewByQuestionUUID.as_view(),
            name='list_answers_by_question_uuid'),
    re_path(r'^answers/c/(?P<uuid>[-\w]+)/$',
            view=q_views.AnswerCreateAPIViewByQuestionUUID.as_view(),
            name='create_answer_by_question_uuid'),
    re_path(r'^answers/$',
            view=q_views.AnswerListCreateApiView.as_view(),
            name='list_answers'),
    re_path(r'^tags/(?P<tag>.+)/$',
            view=q_views.TagQuestionListByTagListApiView.as_view(),
            name='list_questions_by_tag'),
    re_path(r'^tags/$',
            view=q_views.TagListCreateApiView.as_view(),
            name='list_create_tags'),
    re_path(r'^profile/$',
            view=u_views.UseraccountListAPIView.as_view(),
            name='get_user_profile_as_list'),
    re_path(r'^profile/d/(?P<uuid>[-\w]+)/$',
            view=u_views.UseraccountGetUpdateDeleteByUUID.as_view(),
            name='gud_user_profile_by_uuid'),
    ]

