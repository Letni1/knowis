from rest_framework import serializers


from knowis.questions.models import Question, QuestionComment


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'slug', 'content', 'status', 'create_user',
                  'create_date', 'update_date', 'update_user', 'uuid']

class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
