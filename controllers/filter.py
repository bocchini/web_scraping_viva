from bs4 import BeautifulSoup


def parsing(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return search_archive(soup)
    except Exception as error:
        return 'Error to parsing' + str(error)


def search_archive(html_parsing):
    try:
        father_item = html_parsing.find('div', class_='Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block')
        items = father_item.find_all('a')
        links = []
        for link in items:
            links.append(link['href'])
        return links
    except Exception as error:
        return error




