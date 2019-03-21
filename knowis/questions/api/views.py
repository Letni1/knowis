from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveAPIView, RetrieveDestroyAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer
from .permissions import IsOwnerOrReadOnly


class UserQuestionGetList(APIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        try:
            user = self.request.user
            return Question.objects.filter(create_user=user)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request):
        question = self.get_queryset()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuestionGetBySlug(APIView):
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        try:
            slug = self.kwargs['slug']
            queryset = Question.objects.filter(slug=slug)
            return queryset
        except Question.DoesNotExist:
            return Http404

    def get(self, request, slug):
        question = self.get_queryset()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class UserQuestionGetPutDeleteByUUID(APIView):
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        try:
            uuid = self.kwargs['uuid']
            queryset = Question.objects.filter(uuid=uuid)
            return queryset
        except Question.DoesNotExist:
            return Http404

    def get(self, request, uuid):
        question = self.get_queryset()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def delete(self, request, uuid):
        question = self.get_queryset()
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, uuid):
        pass

class QuestionGetList(ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.validated_data['create_user'] = self.request.user
        return super(QuestionGetList, self).perform_create(serializer)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'
