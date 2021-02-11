from playsound import playsound
from os import remove
from random import randint
from gtts import gTTS


class Speaker:
    DEFAULT_LOCALE = 'pt-br'
    DEFAULT_FORMAT = 'mp3'
    FILENAME_BASE = 'audio-'

    def __init__(self, locale=DEFAULT_LOCALE):
        self.locale = locale

    def generate_random_filename(self):
        random_number = randint(0, 100000)
        return f'{self.FILENAME_BASE}{random_number}.{self.DEFAULT_FORMAT}'

    def speak(self, text):
        text_to_speech = gTTS(text=text, lang=self.locale)
        filename = self.generate_random_filename()

        text_to_speech.save(filename)
        playsound(filename)
        remove(filename)

    def play_command_not_found(self):
        self.speak('Não entendi, por favor repita')