from ..models import Question, QuestionComment
from .serializers import QuestionSerializer, QuestionCommentSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



class QuestionGetList(APIView):

