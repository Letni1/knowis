from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer
from .permissions import IsOwnerOrReadOnly


class QuestionListAPIViewByUser(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        queryset = Question.objects.filter(create_user__username=username)
        if queryset:
            return queryset
        else:
            raise NotFound()


class QuestionListAPIViewByMult(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('create_user', 'status')


class QuestionRetrieveUpdateDestroyBySlug(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'


class UserQuestionGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
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
