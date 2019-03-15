from rest_framework import serializers


from ...questions.models import Question, QuestionComment


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'slug', 'content', 'status', 'create_user',
                  'create_date', 'update_date', 'uuid']

    def get_user_questions(self):
        pass


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
