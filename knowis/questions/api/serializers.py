from rest_framework import serializers


from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'slug', 'content', 'status', 'create_user',
                  'create_date', 'update_date', 'update_user', 'uuid']
