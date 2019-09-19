import uuid as uuid_lib

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from uuslug import uuslug


class Useraccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", default="default.jpg")
    avatar_thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 100},
    )
    description = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False
    )

    class Meta:
        db_table = '"useraccount_useraccount"'
        verbose_name = _("Useraccount")
        verbose_name_plural = _("Useraccounts")

    @property
    def username(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = "{} {}".format(
                self.user.first_name, self.user.last_name
            )
            get_slugify = uuslug(slug_str, instance=self)
            self.slug = "-".join(
                name.capitalize() for name in get_slugify.split("-")
            )
        super(Useraccount, self).save(*args, **kwargs)
