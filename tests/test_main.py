import unittest

from fastapi.testclient import TestClient
from main import app, read_titles


class TestMain(unittest.TestCase):
    def test_read_titles(self):
        want = {
            'Cherish',
            'Dr. Dolittle 2',
            'Broken-A Modern Love Story ',
            'Chance- Season 1 ep107',
            'Alcatraz',
            'Boys and Girls',
            'A Smile Like Yours ',
            'Chu Chu and the Philly Flash',
            'Blue Jasmine',
            "Alexander's Ragtime Band",
            'Chance- Season 1 ep103',
            'Bitter Melon',
            'Dark Passage',
            'Bullitt',
            'Always Be My Maybe',
            'Casualties of War',
            'A View to a Kill',
            'Dawn of the Planet of the Apes',
            'After the Thin Man',
            'Escape From Alcatraz',
            '24 Hours on Craigslist',
            'A Smile Like Yours',
            'Dopamine',
            'Ballers Season 3',
            'Copycat',
            'Budding Prospects, Pilot',
            '180',
            'Basic Instinct',
            'Days of Wine and Roses',
            'CSI: NY- episode 903',
            'City of Angels',
            'Beaches',
            'Bee Season',
            'Big Trouble in Little China',
            'Age of Adaline',
            'Bedazzled',
            'Another 48 Hours',
            'Chance - Season 1 Pilot',
            'American Yearbook',
            'Ant-Man',
            'Attack of the Killer Tomatoes',
            'Dim Sum: A Little Bit of Heart',
            'Ant-Man and the Wasp',
            'Dying Young',
            '50 First Dates',
            'Birth of the Dragon',
            'Etruscan Smile',
            'Chance- Season 1 ep102',
            'Broken-A Modern Love Story',
            '40 Days and 40 Nights',
            'Desperate Measures',
            'American Graffiti',
            'A Jitney Elopement',
            'Bicentennial Man',
            'Big Sur',
            'Beautiful Boy',
            'About a Boy',
            'A Night Full of Rain',
            'Chance - Season 1ep105',
            'Burglar',
            'Cardinal X',
            'By Hook or By Crook',
            'Chance Season 2',
            'Chance- Season 1 ep109',
            'Big Eyes',
            'Class Action',
            'Chance- Season 1 ep104',
            'All About Eve',
            'Down Periscope',
            'Barbary Coast',
            'Babies',
            'Chance- Season 1 ep106',
            'Crackers',
            'Common Threads: Stories From the Quilt',
            'A Taiwanese Tale of Two Cities',
            'Edtv',
            'Chance- Season 1 ep110',
            'Chance- Season 1 ep108',
            'Doctor Dolittle',
            '48 Hours',
            'Dirty Harry',
            'Chance - Season 1 ep105',
            'Confessions of a Burning Man',
            'Birdman of Alcatraz',
            'Dream with the Fishes',
            "Can't Stop the Music",
            'Chan is Missing',
            'Dream for an Insomniac',
            'Americana',
            'Around the Fire',
            'D.O.A'
        }

        got = read_titles()

        self.assertEqual(want, got)

    def test_read_server_status(self):
        client = TestClient(app)
        response = client.get('/status')

        want = {
            'status': 'OK',
            'api': 'v1'
        }

        got = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want, got)

    def test_read_home_page(self):
        client = TestClient(app)
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template.name, 'home.html')

    def test_read_movies(self):
        client = TestClient(app)
        data = {'title': 'Alcatraz'}
        response = client.post('/movie-locations', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template.name, 'home.html')


if __name__ == '__main__':
    unittest.main()
