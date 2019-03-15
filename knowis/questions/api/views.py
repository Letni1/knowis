from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserQuestionGetList(APIView):
    def get_query(self):
        try:
            return Question.objects.get(create_user=self.request.user)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_query()
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data)

