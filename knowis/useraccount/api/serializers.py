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

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request is not None and not request.parser_context.get('kwargs'):
            fields.pop('id', None)
        return fields
