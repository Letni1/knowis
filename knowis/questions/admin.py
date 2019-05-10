from django.contrib import admin
from .models import Question, QuestionAnswer, Tag


admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
