from rest_framework import serializers
from ...useraccount.models import Useraccount
from django.contrib.auth.models import  User


class UseraccountSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()

    class Meta:
        model = Useraccount
        fields = '__all__'
