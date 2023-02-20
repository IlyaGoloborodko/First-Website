from django.apps import AppConfig
from django.dispatch import Signal

from .utilities import send_activation_notification


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    # Вместо main выводится verbose_name
    verbose_name = 'Доска объявлений'

# Так как выдает ошибку, заменил это:
# user_registered = Signal(providing_args=['instance'])
# на:
user_registered = Signal()


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)
