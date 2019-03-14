from rest_framework.generics import  (
    ListCreateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from knowis.questions.models import Question
from .serializers import QuestionSerializer


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
