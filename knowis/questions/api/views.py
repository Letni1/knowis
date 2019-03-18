from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# class UserQuestionGetList(APIView):
#     permission_classes = (IsAuthenticated, )
#     serializer_class = QuestionSerializer
#     lookup_field = 'uuid'
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return Question.objects.filter(create_user=user)
#
#     def get(self, request):
#         question = self.get_queryset()
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

class QuestionGetList(ListCreateAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    lookup_field = 'uuid'



