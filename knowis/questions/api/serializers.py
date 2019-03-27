from rest_framework import serializers


from ...questions.models import Question, QuestionComment, Tag


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    tags = serializers.SlugRelatedField(many=True, slug_field='tag',
                                        queryset=Tag.objects.all())

    class Meta:
        model = Question
        fields = '__all__'
        # fields = ('title', 'content', 'status', 'create_date',
        #           'update_date', 'get_create_user', 'uuid', 'slug')

    def to_internal_value(self, data):
        for tag_name in data.get('tags', []):
            Tag.objects.get_or_create(tag=tag_name)
        return super().to_internal_value(data)


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
