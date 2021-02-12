import requests
from os import getenv
from commands.BaseCommand import BaseCommand
from core.exceptions.InvalidCommandParams import InvalidCommandParams
from lib.utils import kelvin_to_celsius


class TemperaturaCommand(BaseCommand):
    BASE_API_URL = 'http://api.openweathermap.org/data/2.5/weather?'

    def __init__(self, params=[]):
        super().__init__(params)

    def get_city_name(self):
        for param in self.params:
            if param.capitalize() == param:
                return param
        return None

    def exec(self):
        api_key = getenv('WEATHER_API_KEY')
        city_name = self.get_city_name()

        if city_name is None:
            raise InvalidCommandParams(self.params)

        response = requests.get(f'{self.BASE_API_URL}q={city_name}&appid={api_key}')
        parsed_response = response.json()

        temperature = kelvin_to_celsius(parsed_response['main']['temp'])
        feels_like = kelvin_to_celsius(parsed_response['main']['feels_like'])

        return f'A temperatura é {temperature} graus celsius e a sensação térmica é de {feels_like} graus celsius '

    def __str__(self):
        return __class__
