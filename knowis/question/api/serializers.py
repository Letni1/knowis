from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.response import Response

from ...questions.models import Question, QuestionAnswer, Tag


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    get_tags = serializers.ListField(
        child=serializers.CharField(), read_only=True
    )
    get_num_answers = serializers.ReadOnlyField()
    get_answers = serializers.ListField(
        child=serializers.CharField(), read_only=True
    )

    class Meta:
        model = Question
        fields = "__all__"

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request")
        if request is not None and not request.parser_context.get("kwargs"):
            fields.pop("id", None)
        return fields


class TagSerializer(serializers.ModelSerializer):
    get_popular_tags = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = "__all__"


class QuestionAnswerSerializer(serializers.ModelSerializer):
    # reply = serializers.SerializerMethodField()
    username = serializers.ReadOnlyField()
    question_uuid = serializers.ReadOnlyField()

    class Meta:
        model = QuestionAnswer
        fields = "__all__"

    # @staticmethod
    # def get_reply(obj):
    #     return [QuestionAnswerSerializer().to_representation(cat)
    #             for cat in obj.reply.all()]

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request")
        if request is not None and not request.parser_context.get("kwargs"):
            fields.pop("id", None)
        return fields
