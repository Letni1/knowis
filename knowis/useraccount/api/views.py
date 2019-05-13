from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ...core.permissions import IsUserOrReadOnly, IsUser
from ..models import Useraccount
from .serializers import UseraccountSerializer


class UseraccountListAPIView(ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UseraccountSerializer

    def get_queryset(self):
        user = self.request.user.id
        queryset = Useraccount.objects.filter(user=user)
        if queryset:
            return queryset
        else:
            raise NotFound()


class UseraccountGetUpdateDeleteByUUID(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy questions by uuid
    """
    permission_classes = (IsUser, IsAuthenticated)
    queryset = Useraccount.objects.all()
    serializer_class = UseraccountSerializer
    lookup_field = 'uuid'


