from django.apps import AppConfig


class WikiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wiki"
    verbose_name = "База для бота-информатора интересных мест"
