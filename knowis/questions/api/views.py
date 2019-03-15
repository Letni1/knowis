from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from ..models import Question
from .serializers import QuestionSerializer

from knowis.questions.models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer



class QuestionListCreatedApiView(ListCreateAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'


class QuestionRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'


class QuestionCommentListCreateAPIView(ListCreateAPIView):
    queryset = QuestionComment.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionCommentSerializer
    lookup_field = 'uuid'


class QuestionCommentDestroyAPIView(RetrieveDestroyAPIView):
    queryset = QuestionComment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionCommentSerializer
    lookup_field = 'uuid'

