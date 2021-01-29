from data.data_files import read_file
from controllers.crawler import search_repository
from controllers.filter import parsing, search_archive

repo = read_file()
html_repository = search_repository(repo[1])

print(parsing(html_repository))
