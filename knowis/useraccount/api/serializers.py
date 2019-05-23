from rest_framework import serializers
from ...useraccount.models import Useraccount
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from django.contrib.auth.models import  User
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError


class UseraccountSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()

    class Meta:
        model = Useraccount
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request is not None and not request.parser_context.get('kwargs'):
            fields.pop('id', None)
        return fields


class ProfileRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

