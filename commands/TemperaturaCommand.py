from commands.BaseCommand import BaseCommand


class TemperaturaCommand(BaseCommand):
    def __init__(self, params=[]):
        super().__init__(params)

    def exec(self):
        print(self.params)
        return 'tá frio'

    def __str__(self):
        return __class__
