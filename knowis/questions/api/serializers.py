from rest_framework import serializers


from ...questions.models import Question, QuestionComment


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = '__all__'
        # fields = ('title', 'content', 'status', 'create_date',
        #           'update_date', 'get_create_user', 'uuid', 'slug')


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
