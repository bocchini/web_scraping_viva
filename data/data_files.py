import json


FILE = 'repositories.txt'
FILE_WRITE = 'details.txt'


def read_file():
    try:
        with open(FILE, 'r') as file:
            data = file.readlines()
            return data
    except FileNotFoundError:
        return 'File no found'


def write_file(data, repository):
    try:

        repository = f'Project_{repository}.text'
        with open(FILE_WRITE, 'w+', encoding='UTF-8') as file:
            file.write(repository)
            file.write('       Extensão     |    Linhas       |     Bytes  \n')
            json.dump(data, file, indent=4)
            return 'Write ok'
    except Exception as error:
        return 'Error to write archive ' + str(error)
