from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.fields import empty

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
        fields = ['title', 'image', 'slug', 'content', 'status',
                  'create_user', 'create_date', 'update_date', 'uuid',
                  'username', 'get_tags', 'get_num_comments', 'get_comments']


class TagSerializer(serializers.ModelSerializer):
    get_popular_tags = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = ['tag', 'question', 'uuid', 'get_popular_tags']


class QuestionCommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = QuestionComment
        fields = ['question', 'replied_to', 'date', 'user', 'upvotes',
                  'uuid', 'reply', 'comment', 'question_uuid']

    @staticmethod
    def get_reply(obj):
        return [QuestionCommentSerializer().to_representation(cat)
                for cat in obj.reply.all()]
