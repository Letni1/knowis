from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated,
                                        AllowAny, IsAuthenticatedOrReadOnly)

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer
from .permissions import IsOwnerOrReadOnly


class QuestionListAPIViewByUser(ListAPIView):
    """
    List the Published questions by username from url, paginated
    """
    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Published questions for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        queryset = Question.objects.filter(
            create_user__username=username
        ).filter(status='P')
        if queryset:
            return queryset
        else:
            raise NotFound()


class QuestionListAPIViewBySlug(ListAPIView):
    """
    List the Published questions by slug from url, paginated
    """
    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Published questions for
        the slug as determined by the slug portion of the URL.
        """
        slug = self.kwargs['slug']
        queryset = Question.objects.filter(
            slug=slug
        ).filter(status='P')
        if queryset:
            return queryset
        else:
            raise NotFound()


class UserQuestionGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy questions by uuid
    """
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'


class QuestionListCreateAPIView(ListCreateAPIView):
    """
    Returns the list of questions with pagination and filtering
    Authenticated user can post questions
    """
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.filter(status='P')
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('create_user', 'tag')

    def perform_create(self, serializer):
        """
        Overwrite create_user field by user logged in.
        """
        serializer.validated_data['create_user'] = self.request.user
        return super(QuestionListCreateAPIView,
                     self).perform_create(serializer)


