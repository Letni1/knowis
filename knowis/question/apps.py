from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = "knowis.questions"
    verbose_name = "Questions"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
