from rest_framework import serializers


from ...questions.models import Question, QuestionComment


class QuestionSerializer(serializers.ModelSerializer):
    get_create_user = serializers.ReadOnlyField()
    title = serializers.CharField()
    class Meta:
        model = Question
        fields = '__all__'
        # fields = ('title', 'slug', 'content', 'status', 'create_user',
        #           'create_date', 'update_date', 'get_create_user', 'uuid')


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
