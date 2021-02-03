from bs4 import BeautifulSoup

from controllers.crawler import search_repository


def access_to_git(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as error:
        return 'Error to parsing' + str(error)


def list_archive_main_page(html_parsing):
    html_parsing = access_to_git(html_parsing)
    try:
        father_item = html_parsing.find('div',
                                        class_='Details-content--hidden-not-important '
                                               'js-navigation-container '
                                               'js-active-navigation-container d-md-block')
        items = father_item.find_all('a')
        links = []
        for link in items:
            links.append(link['href'])
        return links
    except Exception as error:
        return error


def search_pages(page):
    page = access_to_git(page)
    try:
        page = page.find('div',
                         class_='Details-content--hidden-not-important '
                                'js-navigation-container '
                                'js-active-navigation-container d-block')
        items = page.find_all('a')
        link = []
        for item in items:
            link.append(item['href'])
        return link
    except Exception as error:
        return error


def details_archive(link):
    try:
        link = access_to_git(link)
        details = link.find('div',
                            class_='text-mono f6 flex-auto pr-3 flex-order-2 '
                                   'flex-md-order-1 mt-2 mt-md-0')
        return details.text.strip()
    except Exception as error:
        print(error)


def is_file(link):
    try:
        files = []
        for li in link:
            files.append(li.split('/'))

        after = []
        archive = {}
        for number, file in enumerate(files):

            if '.' in file[-1]:
                if link[number] in after:
                    after.remove(link[number])
                result_data_file = (
                    details_archive(search_repository(link[number])))
                if result_data_file is not None:
                    archive[link[number]] = result_data_file
            else:
                after.append(link[number])
        return archive, after
    except Exception as error:
        pass


def folders_in_git(link_folder):
    repository = search_repository(link_folder)
    link = search_pages(repository)
    archive, after = is_file(link)
    print(after)
    return archive, after


def list_archive(link_repository):
    archive = list_archive_main_page(link_repository)
    archive, after = is_file(archive)

    """while len(after) >= 0:
        if len(after) > 0:
            for page in after:
                archive, after = folders_in_git(page)"""

    return archive
