from rest_framework import serializers
from rest_framework.response import Response

from ...questions.models import Question, QuestionComment, Tag


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    get_tags = serializers.ListField(child=serializers.CharField(),
                                     read_only=True)
    get_num_comments = serializers.ReadOnlyField()
    get_comments = serializers.ListField(child=serializers.CharField(),
                                         read_only=True)

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
    children = serializers.SerializerMethodField()

    class Meta:
        model = QuestionComment
        fields = '__all__'


    def validate(self, data):
        pass

    def get_children(self, obj):
        return [QuestionCommentSerializer().to_representation(cat)
                for cat in obj.children.all()]
