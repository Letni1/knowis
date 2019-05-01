from django.urls import re_path
from ..questions.api import views as q_views
from ..useraccount.api import views as u_views


app_name = 'api'

urlpatterns = [
    re_path(r'^questions/u/(?P<username>.+)/$',
            view=q_views.QuestionListAPIViewByUser.as_view(),
            name='questions_by_user'
            ),
    re_path(r'^questions/d/(?P<slug>.+)/$',
            view=q_views.UserQuestionGetUpdateDeleteBySlug.as_view(),
            name='questions_by_slug'
    re_path(r'^questions/d/(?P<uuid>[-\w]+)/$',
            view=q_views.UserQuestionGetUpdateDeleteByUUID.as_view(),
            name='questions_delete'),
    re_path(r'^questions/(?P<slug>.+)/$',
            view=q_views.QuestionListAPIViewBySlug.as_view(),
            name='questions_by_slug'
            ),
    re_path(r'^questions/$', view=q_views.QuestionListCreateAPIView.as_view(),
            name='questions_rest_api'),
    # re_path(r'^questions/$', view=views.QuestionListAPIViewByMult.as_view(),
    #         name='questions_filter_api'),
    re_path(r'^comments/d/(?P<uuid>[-\w]+)/$',
            view=q_views.UserCommentGetUpdateDeleteByUUID.as_view(),
            name='questions_delete'),
    re_path(r'^comments/$',
            view=q_views.CommentListCreateApiView.as_view(),
            name='questions_delete'),
    re_path(r'^Tags/(?P<tag>.+)/$',
            view=q_views.TagQuestionListByTagListApiView.as_view(),
            name='questions_by_tag'),
    re_path(r'^Tags/$',
            view=q_views.TagListCreateApiView.as_view(),
            name='tags'),
    re_path(r'^profile/$',
            view=u_views.UseraccountListAPIView.as_view(),
            name='user_list'),
    re_path(r'^profile/d/(?P<uuid>[-\w]+)/$',
            view=u_views.UseraccountGetUpdateDeleteByUUID.as_view(),
            name='user_ud')
]
