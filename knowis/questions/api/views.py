from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveAPIView, RetrieveDestroyAPIView,
                                     GenericAPIView)
from rest_framework import mixins
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


class QuestionGetBySlug(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    slug = kwargs['']
    queryset = Question.objects.filter(slug=slug)
    # def get_object(self, slug):
    #     try:
    #         question = Question.objects.get(slug=slug)
    #         return question
    #     except Question.DoesNotExist:
    #         return Http404
    #
    # def get(self, request, slug, format=None):
    #     question = self.get_object(slug=slug)
    #     serializer = QuestionSerializer(question, many=True)
    #     return Response(serializer.data)
    #
    # def delete(self, request, slug):
    #     question = self.get_object(slug=slug)
    #     question.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def put(self, request, slug):
    #     question = self.get_object(slug)
    #     serializer = QuestionSerializer(question, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserQuestionGetPutDeleteByUUID(APIView):
    permission_classes = (IsOwnerOrReadOnly, )

    def get_object(self, uuid):
        try:
            queryset = Question.objects.filter(uuid=uuid)
            return queryset
        except Question.DoesNotExist:
            return Http404

    def get(self, request, uuid):
        question = self.get_object(uuid=uuid)
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def delete(self, request, uuid):
        question = self.get_object(uuid=uuid)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, uuid):
        question = self.get_object(uuid=uuid)


class QuestionListCreateAPIView(ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.validated_data['create_user'] = self.request.user
        return super(QuestionListCreateAPIView,
                     self).perform_create(serializer)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'
