FILE = 'repositories.txt'


def read_file():
    try:
        with open(FILE, 'r') as file:
            data = file.readlines()
            return data
    except FileNotFoundError:
        return 'File no found'


def write_file(data):
    try:
        with open(data, 'w+') as file:
            file.write(data)
            return 'Write ok'
    except Exception as error:
        return 'Error to write archive ' + str(error)
