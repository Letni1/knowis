import markdown
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..users.models import User
from datetime import datetime
from django.template.defaultfilters import slugify


class Question(models.Model):
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
    update_user = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)

    class Meta:
        db_table = '"questions"'
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ("-create_date",)
