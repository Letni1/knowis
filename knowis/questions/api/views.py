from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer
from .permissions import IsOwnerOrReadOnly


class UserQuestionGetList(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = QuestionSerializer
    pass



class QuestionRetrieveUpdateDestroyBySlug(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'


class UserQuestionGetUpdateDeleteByUUID(QuestionRetrieveUpdateDestroyBySlug):
    lookup_field = 'uuid'


class QuestionListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        serializer.validated_data['create_user'] = self.request.user
        return super(QuestionListCreateAPIView,
                     self).perform_create(serializer)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'
