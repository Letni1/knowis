from rest_framework import serializers
from rest_framework.response import Response

from ...questions.models import Question, QuestionComment, Tag


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    get_tags = serializers.ListField()
    get_num_comments = serializers.ReadOnlyField()
    get_comments = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Question
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    get_popular_tags = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    question_title = serializers.ReadOnlyField()

    class Meta:
        model = QuestionComment
        fields = '__all__'

    # def to_representation(self, obj):
    #     ret = super(QuestionCommentSerializer, self).to_representation(obj)
    #     if
