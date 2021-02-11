class CommandNotFoundException(Exception):
    def __init__(self, command_name):
        super().__init__(f'Could not found command {command_name}')
