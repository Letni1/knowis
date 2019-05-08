from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..models import Question, QuestionComment, Tag
from .serializers import (QuestionSerializer, QuestionCommentSerializer,
                          TagSerializer)
from ...core.permissions import IsOwnerOrReadOnly, IsUserOrReadOnly


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


class UserQuestionGetUpdateDeleteBySlug(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy questions by slug
    """
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'slug'


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
    Returns the list of questions with pagination and filtering by tags/user

    """
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination
    queryset = Question.objects.filter(status='P')
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('create_user', )

    def perform_create(self, serializer):
        """
        Overwrite create_user field by user logged in.
        """
        serializer.validated_data['create_user'] = self.request.user
        return super(QuestionListCreateAPIView,
                     self).perform_create(serializer)


class CommentListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer
    lookup_field = 'uuid'

    def perform_create(self, serializer):
        """
        Overwrite create_user field by user logged in.
        """
        serializer.validated_data['user'] = self.request.user
        return super(CommentListCreateApiView,
                     self).perform_create(serializer)


class CommentCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, uuid):
        try:
            return Question.objects.get(uuid=uuid)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        questions = self.get_object(uuid)
        serializer = QuestionSerializer(questions)
        print(serializer.data['id'])
        return Response({
            "id": serializer.data['id']
        })

    def post(self, request, uuid, format=None):
        questions = self.get_object(uuid)
        question_serializer = QuestionSerializer(questions)
        serializer = QuestionCommentSerializer(data={
            "question": question_serializer.data['id'],
            "user": request.user.id,
            "comment": request.GET.get('comment', '')
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommentListApiViewByUUID(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    serializer_class = QuestionCommentSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        queryset = QuestionComment.objects.filter(
            question__uuid=uuid
        )
        if queryset:
            return queryset
        else:
            raise NotFound()


class UserCommentGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy questions by uuid
    """
    permission_classes = (IsUserOrReadOnly, )
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer
    lookup_field = 'uuid'


class TagListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'uuid'


class TagQuestionListByTagListApiView(ListAPIView):
    """
        List the Published questions by tag from url, paginated
    """
    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Published questions for
        the tag as determined by the tag portion of the URL.
        """
        tag = self.kwargs['tag']
        queryset = Question.objects.filter(
            tag=tag
        ).filter(status='P')
        if queryset:
            return queryset
        else:
            raise NotFound()
