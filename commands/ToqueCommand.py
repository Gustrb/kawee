import pywhatkit
from commands.BaseCommand import BaseCommand


class ToqueCommand(BaseCommand):
    def __init__(self, params=[]):
        super().__init__(params)

    def exec(self):
        content_to_search = ' '.join(self.params)

        pywhatkit.playonyt(content_to_search)
        return f'Tocando {content_to_search}'

    def __str__(self):
        return __class__
