from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Useraccount


@receiver(post_save, sender=User)
def create_useraccount(sender, instance, created, **kwargs):
    if created:
        Useraccount.objects.create(user=instance)
