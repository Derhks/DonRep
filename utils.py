import json

from requests import get, exceptions
from settings import GOOGLE_ENDPOINT, GOOGLE_API_KEY


def get_coordinates(title: str) -> tuple:
    try:
        title = title.replace(' ', '+')
        url = GOOGLE_ENDPOINT + title + '&key=' + GOOGLE_API_KEY
        response = get(url=url)

        dict_body = json.loads(response.content.decode('utf-8'))

        if dict_body['status'] == 'OK':
            lat = dict_body['results'][0]['geometry']['location']['lat']
            lng = dict_body['results'][0]['geometry']['location']['lng']
        else:
            lat = 0
            lng = 0

        return lat, lng

    except exceptions.HTTPError as Err:
        raise Err
