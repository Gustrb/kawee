from importlib import import_module
from json import JSONDecoder
from lib.utils import init_dotenv, remove_special_chars, add_command_suffix

from core.SpeechRecognizer import SpeechRecognizer
from core.Speaker import Speaker
from core.exceptions.CommandNotFoundException import CommandNotFoundException
from core.exceptions.InvalidCommandParams import InvalidCommandParams


class Kawee:
    COMMANDS_MODULE = 'commands'
    JSON_COMMANDS_PATH = './commands.json'

    def __init__(self):
        init_dotenv()

        self.speech_recognizer = SpeechRecognizer()
        self.speaker = Speaker()

        self.start()

    def start(self):
        text = self.listen()

        try:
            data_to_speak = self.select_command(text)
            self.speaker.speak(data_to_speak)

        except CommandNotFoundException:
            self.speaker.play_command_not_found()
        
        except InvalidCommandParams:
            self.speaker.play_invalid_params()

    def listen(self):
        while True:
            text = self.speech_recognizer.listen()

            if text is None:
                print('Não entendi...')
                continue

            return text

    def import_module(self, module_name):
        module = import_module(f"{self.COMMANDS_MODULE}.{module_name}")
        class_ = getattr(module, module_name)

        return class_

    def load_created_commands(self):
        with open(self.JSON_COMMANDS_PATH, 'r') as f:
            file_content = f.read()
        
        return (JSONDecoder().decode(file_content))['commands']
    
    def select_command(self, text):
        parsed_text = remove_special_chars(text)
        text_words = parsed_text.split(' ')
        
        created_commands = self.load_created_commands()

        for command in created_commands:
            for word in text_words:
                if command == word.lower():
                    module_name = add_command_suffix(word.capitalize())
                    untreated_class = self.import_module(module_name)
                    text_words.remove(word)
                    instance = untreated_class(text_words)

                    return instance.exec()
        
        raise CommandNotFoundException(command_name=parsed_text)
