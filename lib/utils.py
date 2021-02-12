from dotenv import load_dotenv
from unicodedata import normalize
import math


def kelvin_to_celsius(k):
    return math.trunc(k - 273.15)


def init_dotenv():
    load_dotenv()


def remove_special_chars(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')


def add_command_suffix(text):
    return text + 'Command'
