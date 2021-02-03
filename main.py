import asyncio

from data.data_files import read_file
from controllers.scanning import Scanning

repo = read_file()

scanning = Scanning(repo[0])
html_repository = scanning.get_repository_list()
for html in html_repository.items():
    print(html)
