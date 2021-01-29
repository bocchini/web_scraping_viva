from requests import get as requests_get

URL = 'https://www.github.com/'


def search_repository(repository):
    try:
        repository = URL + repository.strip()
        response = requests_get(repository)

        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            return 'Repository no found'
        else:
            return 'Error in repository'
    except Exception as error:
        return error
