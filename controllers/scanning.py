def get_search(page, pattern=None):
    list_page = page.find('div', class_=pattern)
    if list_page is None:
        return
    text_repository = []

    for details_html in list_page.find_all('a'):
        text_repository.append(details_html['href'])
    return text_repository


class Scanning:
    archive_information = {}

    def __init__(self, repository_to_scanning):
        self.repository_to_scanning = repository_to_scanning
        self.folder_in_repository = set()
        self.archive_repository = set()

    def get_data_of_repository_list(self):
        html_parser = self.parsing_to_soup(self.repository_to_scanning)
        self.main_page_list(html_parser)
        self.other_pages()
        self.information_archive(self.archive_repository)
        from controllers.accountant_files import AccountantFiles
        account_files = AccountantFiles()
        details = account_files.details_files(self.archive_information)
        return details

    def access_to_page(self, page):
        from controllers.crawler import search_repository
        repository = search_repository(page)
        return repository

    def parsing_to_soup(self, page):
        try:
            from bs4 import BeautifulSoup
            page = self.access_to_page(page)
            html_parser = BeautifulSoup(page, 'html.parser')
            return html_parser
        except Exception as error:
            return error

    def main_page_list(self, main_page):
        text_repository = get_search(main_page,
                                     'Details-content--hidden-not-important '
                                     'js-navigation-container '
                                     'js-active-navigation-container d-md-block')

        self.separate_folder_archive(text_repository)

    def list_data_in_folder(self, page):
        try:

            text_repository = get_search(page,
                                              'Details-content--hidden-not-important '
                                              'js-navigation-container '
                                              'js-active-navigation-container '
                                              'd-block')
            del text_repository[0]
            self.separate_folder_archive(text_repository)
        except Exception as error:
            print(error)

    def separate_folder_archive(self, repositories):
        repositories_copy = self.folder_in_repository.copy()
        for repository in repositories:
            repository_separade = str(repository).split('/')
            if 'commit' in repository_separade[-2] or 'LICENSE' in \
                    repository_separade[-1]:
                pass
            elif '.' in repository_separade[-1]:
                self.archive_repository.add(repository)
                if self.folder_in_repository in self.folder_in_repository:
                    del self.folder_in_repository
            else:
                repositories_copy.add(repository)

        self.folder_in_repository = repositories_copy.copy()
        if len(self.folder_in_repository) < 1:
            self.other_pages()

    def other_pages(self):
        for page in self.folder_in_repository:
            pages = self.parsing_to_soup(page)
            self.list_data_in_folder(pages)

    def details_archive(self, details):
        data = []
        for detail in details:
            data.append(detail.split('('))
        return data[0][0], data[-1]

    def information_archive(self, archive_link):
        information = dict()
        for archive in archive_link:
            page = self.parsing_to_soup(archive)

            try:
                list_page = page.find('div',
                                      class_='text-mono f6 flex-auto pr-3 '
                                             'flex-order-2 flex-md-order-1 '
                                             'mt-2 mt-md-0')

                detail = list_page.text.strip().split('\n')
                details = self.details_archive(detail)
                information[archive] = details

                self.archive_information[archive] = details

            except Exception as error:
                print(error)

