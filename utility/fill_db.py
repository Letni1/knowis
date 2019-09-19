import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from knowis.question.models import Question
from django.contrib.auth.models import User

bob = User.objects.get_or_create(username='bob')
user = User.objects.get(username='bob')
for i in range(100):
    Question.objects.create(title='Test_{}'.format(i), content='Test_content_{}'.format(i), status='P', create_user=user)
