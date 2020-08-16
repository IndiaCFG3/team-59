from django.apps import AppConfig


class PannahConfig(AppConfig):
    name = 'pannah'
    def ready(self):
        import pannah.signals