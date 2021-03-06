from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from ...core.permissions import IsOwnerOrReadOnly, IsUserOrReadOnly
from ..models import Question, QuestionAnswer, Tag
from .serializers import (
    QuestionAnswerSerializer,
    QuestionSerializer,
    TagSerializer,
)


class QuestionListAPIViewByUser(ListAPIView):
    """
    List the Published question by username from url, paginated
    """

    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Published question for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs["username"]
        queryset = Question.objects.filter(
            create_user__username=username
        ).filter(status="P")
        if queryset:
            return queryset
        else:
            raise NotFound()


class QuestionListAPIViewBySlug(ListAPIView):
    """
    List the Published question by slug from url, paginated
    """

    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Published question for
        the slug as determined by the slug portion of the URL.
        """
        slug = self.kwargs["slug"]
        queryset = Question.objects.filter(slug=slug).filter(status="P")
        if queryset:
            return queryset
        else:
            raise NotFound()


class UserQuestionGetUpdateDeleteBySlug(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy question by slug
    """

    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = "slug"


class UserQuestionGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy question by uuid
    """

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "uuid"


class QuestionListAPIView(ListAPIView):
    """
    Returns the list of question with pagination and filtering by tags/user

    """

    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "uuid"
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("create_user",)


class QuestionPostAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = QuestionSerializer(
            data={
                "title": request.GET.get("title", ""),
                "content": request.GET.get("content", ""),
                "create_user": request.user.id,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerCreateAPIViewByQuestionUUID(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, uuid):
        try:
            return Question.objects.get(uuid=uuid)
        except Question.DoesNotExist:
            raise Http404

    def post(self, request, uuid, format=None):
        questions = self.get_object(uuid)
        question_serializer = QuestionSerializer(questions)
        serializer = QuestionAnswerSerializer(
            data={
                "question": question_serializer.data["id"],
                "user": request.user.id,
                "answer": request.GET.get("answer", ""),
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy question by uuid
    """

    permission_classes = (IsUserOrReadOnly,)
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    lookup_field = "uuid"


class AnswerListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    lookup_field = "uuid"


class AnswersListApiViewByQuestionUUID(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    serializer_class = QuestionAnswerSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        uuid = self.kwargs["uuid"]
        queryset = QuestionAnswer.objects.filter(question__uuid=uuid)
        if queryset:
            return queryset
        else:
            raise NotFound()


class TagListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "uuid"


class TagQuestionListByTagListApiView(ListAPIView):
    """
        List the Published question by tag from url, paginated
    """

    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Published question for
        the tag as determined by the tag portion of the URL.
        """
        tag = self.kwargs["tag"]
        queryset = Question.objects.filter(tag=tag).filter(status="P")
        if queryset:
            return queryset
        else:
            raise NotFound()
