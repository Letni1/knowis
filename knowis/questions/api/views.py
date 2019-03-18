from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status


class UserQuestionGetList(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        try:
            username = self.kwargs['create_user']
            return Question.objects.filter(create_user__username=username)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, username):
        question = self.get_queryset()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuestionGetList(ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.validated_data['create_user'] = self.request.user
        return super(QuestionGetList, self).perform_create(serializer)


    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'



