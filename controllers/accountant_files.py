class AccountantFiles:
    def __init__(self):
        self.extension = dict()
        self.details = {}

    def details_files(self, archive_with_details):
        for archive in archive_with_details.items():
            extension = archive[0].split('.')
            self.counter_extension(extension[1], archive[-1])
        self.percentage_archives_lines()
        return self.detail

    def counter_extension(self, extensions, details):
        detail = ''.join(str(v) for v in details)
        data = detail.split(' ')

        try:
            lines = int(data[0])
            size = int(data[-2])
            if extensions in self.extension.keys():
                self.extension[extensions] = [lines + int(
                    self.extension[extensions][0]), size + int(
                    self.extension[extensions][1])]
            else:
                self.extension[extensions] = [lines, size]
        except ValueError as error:
            pass

    def percentage_archives_lines(self):
        another_value = 0
        another_bytes = 0
        value = 0
        valor = {}
        byte = 0

        for detail in self.extension.items():
            value = value + int(detail[1][0])
            byte = byte + int(detail[1][1])
        for detail in self.extension.items():
            if detail[0] == 'gitignore' or detail[0] == 'Dockerfile' \
                    or detail[0] == 'Makefile':
                another_value = int(detail[1][0]) + another_value
                another_bytes = int(detail[1][1]) + another_bytes
            else:
                valor[detail[0]] = [f'{detail[1][0]} (' + str(
                    int((int(detail[1][0]) * 100) / value)) + ' %)',
                                    f'{detail[1][1]} (' + str(
                                        int((int(detail[1][
                                                     1]) * 100) / byte)) +
                                    ' %)']

        valor['outros'] = [
            f'{another_value} (' + str(int(another_value * 100 / value)) +
            ' %)',
            f'{another_bytes} (' + str(int(another_bytes * 100 / byte)) +
            ' %)']

        self.detail = dict(valor)
