from commands.BaseCommand import BaseCommand


class OlaCommand(BaseCommand):
    def __init__(self, params=[]):
        super().__init__()

    def exec(self):
        return 'Olá!'

    def __str__(self):
        return __class__
