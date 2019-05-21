import markdown
import logging
from unidecode import unidecode
import uuid as uuid_lib
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from uuslug import uuslug
from django.forms.models import model_to_dict


class Question(models.Model):
    name = 'Question'
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=5000, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)
    # update_user = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    class Meta:
        db_table = '"question_questions"'
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ("-create_date",)

    def __str__(self):
        return self.title

    @property
    def username(self):
        return self.create_user.get_username()

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = "{}".format(self.title.lower())
            self.slug = uuslug(slug_str, instance=self)
        super(Question, self).save(*args, **kwargs)

    def get_tags(self):
        return Tag.objects.filter(question=self)

    def get_num_answers(self):
        return len(QuestionAnswer.objects.filter(question=self))


class Tag(models.Model):
    tag = models.CharField(max_length=64)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    class Meta:
        db_table = '"question_tags"'
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        unique_together = (('tag', 'question'),)
        index_together = [['tag', 'question'], ]

    def __str__(self):
        return self.tag

    @staticmethod
    def get_popular_tags():
        tags = Tag.objects.all()
        count = {}
        for tag in tags:
            if tag.question.status == Question.PUBLISHED:
                if tag.tag in count:
                    count[tag.tag] = count[tag.tag] + 1
                else:
                    count[tag.tag] = 1
        sorted_count = sorted(count.items(), key=lambda t: t[1], reverse=True)
        return sorted_count[:20]


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    # replied_to = models.ForeignKey("self", related_name='reply',
    #                                on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    class Meta:
        db_table = '"question_answers"'
        verbose_name = _("Question Answer")
        verbose_name_plural = _("Question Answers")
        ordering = ("upvotes", "date")

    @property
    def question_title(self):
        return self.question.title

    @property
    def question_uuid(self):
        return self.question.uuid

    @property
    def username(self):
        return self.user.username


class UserUpvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    class Meta:
        db_table = '"question_upvotes"'
