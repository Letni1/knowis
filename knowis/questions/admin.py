from django.contrib import admin
from .models import Question, QuestionComment, Tag


admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(Tag)
