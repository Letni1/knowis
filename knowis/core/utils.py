from rest_framework import serializers
from django.

class RemovedIdSerializer(serializers.ModelSerializer):

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request")
        if request is not None and not request.parser_context.get("kwargs"):
            fields.pop("id", None)
        return fields
