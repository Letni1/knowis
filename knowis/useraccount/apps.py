from django.apps import AppConfig


class UseraccountConfig(AppConfig):
    name = "knowis.useraccount"
    verbose_name = "Useraccount"

    def ready(self):
        try:
            import knowis.useraccount.signals.handlers  # noqa F401
        except ImportError:
            pass
