import sys
import os
import json


COMMAND_SUFFIX = 'Command'
COMMANDS_FOLDER = './commands'
COMMANDS_JSON_PATH = './commands.json'


def add_suffix(text):
    return f'{text}{COMMAND_SUFFIX}.py'


def get_filename():
    filename = sys.argv[1].capitalize()

    return add_suffix(f'{filename}')


def create_file():
    filename = get_filename()
    file_path = f'{COMMANDS_FOLDER}/{filename}'

    if os.path.isfile(file_path):
        print(f'File {filename} already exists')
        return

    with open(file_path, 'w') as f:
        pass

    parsed_file_content = ''
    with open(COMMANDS_JSON_PATH, 'r') as f:
        file_content = f.read()
        parsed_file_content = json.JSONDecoder().decode(file_content)

    parsed_file_content['commands'].append(sys.argv[1])

    with open(COMMANDS_JSON_PATH, 'w') as f:
        f.write(json.JSONEncoder().encode(parsed_file_content))

    print(f'Comando {sys.argv[1]} criado com sucesso!')


create_file()
