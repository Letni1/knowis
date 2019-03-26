import markdown
import uuid as uuid_lib
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import slugify


class Question(models.Model):
    name = 'Question'
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
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
            self.slug = slugify(slug_str)
        super(Question, self).save(*args, **kwargs)


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = '"question_tags"'
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        unique_together = (('tag', 'question'),)
        index_together = [['tag', 'question'], ]

    def ___str__(self):
        return self.tag


class QuestionComment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
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
        verbose_name = _("Question Comment")
        verbose_name_plural = _("Question Comments")
        ordering = ("date",)


class UserUpvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(QuestionComment, on_delete=models.CASCADE)

    class Meta:
        db_table = '"question_upvotes"'
