class BaseCommand:
    def __init__(self, params=[]):
        self.params = params

    def exec(self):
        pass

    def __str__(self):
        pass
