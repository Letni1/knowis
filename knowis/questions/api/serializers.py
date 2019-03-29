from rest_framework import serializers
from rest_framework.response import Response

from ...questions.models import Question, QuestionComment, Tag


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    tags = serializers.SlugRelatedField(many=True, slug_field='tag',
                                        queryset=Tag.objects.all())
    get_num_comments = serializers.ReadOnlyField()
    get_comments = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Question
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    question_title = serializers.ReadOnlyField()

    class Meta:
        model = QuestionComment
        fields = '__all__'

