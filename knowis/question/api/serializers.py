from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.response import Response
from ...question.models import Question, QuestionAnswer, Tag
from ...core.utils import RemovedIdSerializer


class QuestionSerializer(RemovedIdSerializer):
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



class TagSerializer(serializers.ModelSerializer):
    get_popular_tags = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = "__all__"


class QuestionAnswerSerializer(RemovedIdSerializer):
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
