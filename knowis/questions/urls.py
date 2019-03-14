from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from .api import views



app_name = 'questions'

urlpatterns = [
    re_path(r'^api/$', view=views.QuestionListCreatedApiView.as_view(),
            name='questions_rest_api'),
    re_path(r'^api/(?P<uuid>[-\w]+)/$',
            view=views.QuestionRetrieveDestroyAPIView.as_view(),
            name='question_rest_api'
            )
]
