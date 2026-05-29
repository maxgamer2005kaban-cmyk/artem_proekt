from django.apps import AppConfig


class TrainingConfig(AppConfig):
    """Configuration for the training app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'training'
    verbose_name = 'Training Platform'