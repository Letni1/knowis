from django.urls import re_path

from ..question.api import views as question_views
from ..useraccount.api import views as user_views

app_name = "api_urls"

urlpatterns = [
    re_path(
        r"^question/create/$",
        view=question_views.QuestionPostAPIView.as_view(),
        name="create_question",
    ),
    re_path(
        r"^question/list/$",
        view=question_views.QuestionListAPIView.as_view(),
        name="list_published_questions",
    ),
    re_path(
        r"^question/u/(?P<username>.+)/$",
        view=question_views.QuestionListAPIViewByUser.as_view(),
        name="list_questions_by_username",
    ),
    re_path(
        r"^question/d/(?P<slug>.+)/$",
        view=question_views.UserQuestionGetUpdateDeleteBySlug.as_view(),
        name="get_update_delete_question_by_slug",
    ),
    # re_path(r'^question/d/(?P<uuid>[-\w]+)/$',
    #         view=question_views.UserQuestionGetUpdateDeleteByUUID.as_view(),
    #         name='questions_delete'),
    re_path(
        r"^question/(?P<slug>.+)/$",
        view=question_views.QuestionListAPIViewBySlug.as_view(),
        name="get_question_by_slug",
    ),
    re_path(
        r"^answer/d/(?P<uuid>[-\w]+)/$",
        view=question_views.AnswerGetUpdateDeleteByUUID.as_view(),
        name="answer_delete",
    ),
    re_path(
        r"^answer/q/(?P<uuid>[-\w]+)/$",
        view=question_views.AnswersListApiViewByQuestionUUID.as_view(),
        name="list_answers_by_question_uuid",
    ),
    re_path(
        r"^answer/c/(?P<uuid>[-\w]+)/$",
        view=question_views.AnswerCreateAPIViewByQuestionUUID.as_view(),
        name="create_answer_by_question_uuid",
    ),
    re_path(
        r"^answer/list/$",
        view=question_views.AnswerListCreateApiView.as_view(),
        name="list_answers",
    ),
    re_path(
        r"^tag/(?P<tag>.+)/$",
        view=question_views.TagQuestionListByTagListApiView.as_view(),
        name="list_questions_by_tag",
    ),
    re_path(
        r"^tag/create/$",
        view=question_views.TagListCreateApiView.as_view(),
        name="list_create_tags",
    ),
    re_path(
        r"^account/(?P<slug>.+)/$",
        view=user_views.UseraccountRetrieveBySlug.as_view(),
        name="retrieve_user_account_by_slug",
    ),
    re_path(
        r"^account/$",
        view=user_views.UseraccountListAPIView.as_view(),
        name="get_user_account",
    ),
    re_path(
        r"^account/d/(?P<uuid>[-\w]+)/$",
        view=user_views.UseraccountGetUpdateDeleteByUUID.as_view(),
        name="get_user_account_by_uuid",
    ),
]
