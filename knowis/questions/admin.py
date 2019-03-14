from django.contrib import admin
from .models import Question, QuestionComment


admin.site.register(Question)
admin.site.register(QuestionComment)
