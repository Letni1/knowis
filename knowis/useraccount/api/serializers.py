from rest_framework import serializers
from ...useraccount.models import Useraccount


class UseraccountSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = Useraccount
        fields = '__all__'
