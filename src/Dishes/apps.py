from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class DishesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Dishes'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'