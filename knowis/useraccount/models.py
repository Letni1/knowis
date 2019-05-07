from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid as uuid_lib
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Useraccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='default.jpg')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(200, 200)],
                                      format='JPEG',
                                      options={'quality': 100})
    description = models.TextField(max_length=500, null=True, blank=True)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    class Meta:
        db_table = '"useraccount_useraccount"'
        verbose_name = _("Useraccount")
        verbose_name_plural = _("Useraccounts")

    @property
    def username(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_useraccount(sender, instance, created, **kwargs):
    if created:
        Useraccount.objects.create(user=instance)

