# Generated by Django 2.0.13 on 2019-09-19 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import knowis.question.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, validators=[knowis.question.models.validate_draftjs_not_blank])),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='images/%Y/%m/%d')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, max_length=1500)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'db_table': '"question_questions"',
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5000, validators=[knowis.question.models.validate_draftjs_not_blank])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question Answer',
                'verbose_name_plural': 'Question Answers',
                'db_table': '"question_answers"',
                'ordering': ('upvotes', 'date'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=64)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': '"question_tags"',
            },
        ),
        migrations.CreateModel(
            name='UserUpvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.QuestionAnswer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '"question_upvotes"',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('tag', 'question')},
        ),
        migrations.AlterIndexTogether(
            name='tag',
            index_together={('tag', 'question')},
        ),
    ]