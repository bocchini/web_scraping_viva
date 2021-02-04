from data.data_files import read_file, write_file
from controllers.scanning import Scanning


def initialize():
    repo = read_file()

    scanning = Scanning(repo[0])
    html_repository = scanning.get_data_of_repository_list()
    print(write_file(html_repository, repo[0]))


initialize()
