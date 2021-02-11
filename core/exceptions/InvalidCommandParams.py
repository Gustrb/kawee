class InvalidCommandParams(Exception):
    def __init__(self, given_params):
        super().__init__(f'Temperature params must include a city name. Params given: {given_params}')
