from datetime import datetime
import json
import logging
import uuid as uuid_lib

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
import markdown
from unidecode import unidecode
from uuslug import uuslug


def validate_draftjs_not_blank(field):
    try:
        text = json.loads(field)
        text_len = len("".join(i["text"] for i in text["blocks"]))
        if text_len <= 0:
            raise ValidationError(
                _("%(field) не може бути пустим"), params={"field": field}
            )
    except json.decoder.JSONDecodeError:
        pass


class Question(models.Model):
    name = "Question"
    DRAFT = "D"
    PUBLISHED = "P"
    STATUS = ((DRAFT, "Draft"), (PUBLISHED, "Published"))

    title = models.CharField(
        max_length=500, validators=[validate_draftjs_not_blank]
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d", blank=True, max_length=255
    )
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=1500, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)
    # update_user = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False
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
            try:
                editor_title = json.loads(self.title)
                slug_str = "".join(i["text"] for i in editor_title["blocks"])
            except json.decoder.JSONDecodeError:
                slug_str = "".join(self.title.lower())
            self.slug = uuslug(slug_str, instance=self)
        super(Question, self).save(*args, **kwargs)

    def get_tags(self):
        return Tag.objects.filter(question=self)

    def get_num_answers(self):
        return len(QuestionAnswer.objects.filter(question=self))

    def create_tags(self, tag_list):
        for tag in tag_list:
            if tag:
                t, created = Tag.objects.get_or_create(
                    tag=tag.lower(), question=self
                )


class Tag(models.Model):
    tag = models.CharField(max_length=64)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False
    )

    class Meta:
        db_table = '"question_tags"'
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        unique_together = (("tag", "question"),)
        index_together = [["tag", "question"]]

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
    answer = models.CharField(
        max_length=5000, blank=False, validators=[validate_draftjs_not_blank]
    )
    # replied_to = models.ForeignKey("self", related_name='reply',
    #                                on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False
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

    def get_upvoters(self):
        upvotes = UserUpvote.objects.filter(answer=self)
        upvote_users = [upvote.user.uuid for upvote in upvotes]
        return upvote_users


class UserUpvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False
    )

    class Meta:
        db_table = '"question_upvotes"'
