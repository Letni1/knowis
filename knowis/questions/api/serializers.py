from rest_framework import serializers


from ...questions.models import Question, QuestionComment


class QuestionSerializer(serializers.ModelSerializer):
    get_create_user = serializers.ReadOnlyField()
    class Meta:
        model = Question
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
