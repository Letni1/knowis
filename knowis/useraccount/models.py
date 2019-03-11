from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Useraccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        pass
