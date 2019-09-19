from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ...core.permissions import IsUser, IsUserOrReadOnly
from ..models import Useraccount
from .serializers import UseraccountSerializer


class UseraccountListAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UseraccountSerializer

    def get_object(self, user):
        try:
            return Useraccount.objects.get(user=user)
        except Useraccount.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = self.request.user.id
        current_user = self.get_object(user)
        serializer = UseraccountSerializer(current_user)
        return Response(serializer.data)


class UseraccountGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy question by uuid
    """

    permission_classes = (IsUser, IsAuthenticated)
    queryset = Useraccount.objects.all()
    serializer_class = UseraccountSerializer
    lookup_field = "uuid"


class UseraccountRetrieveBySlug(RetrieveAPIView):
    permission_classes = (IsUser, IsAuthenticated)
    queryset = Useraccount.objects.all()
    serializer_class = UseraccountSerializer
    lookup_field = "slug"
