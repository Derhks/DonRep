from fastapi import Body, FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from settings import SODAPY_APPTOKEN, GOOGLE_API_KEY, SODAPY_DOMAIN, SODAPY_DATASET_IDENTIFIER
from sodapy import Socrata
from utils import get_coordinates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

socrata_domain = SODAPY_DOMAIN
socrata_dataset_identifier = SODAPY_DATASET_IDENTIFIER
socrata_token = SODAPY_APPTOKEN


def read_titles():
    client = Socrata(socrata_domain, socrata_token)
    dataset = client.get(socrata_dataset_identifier)

    titles = []

    for movie in dataset:
        titles.append(movie['title'])

    return set(titles)


@app.get('/status', response_class=JSONResponse)
def read_server_status():
    return {
        'status': 'OK',
        'api': 'v1'
    }


@app.get('/', response_class=HTMLResponse)
def read_home_page(request: Request):
    titles = read_titles()

    return templates.TemplateResponse('home.html', {
        'request': request,
        'API_KEY': GOOGLE_API_KEY,
        'titles': titles
    })


@app.post('/movie-locations', response_class=HTMLResponse)
def read_movies(request: Request, title: str = Body(...)):
    titles = read_titles()
    title = title.replace('+', ' ')[6:]
    client = Socrata(socrata_domain, socrata_token)
    dataset = client.get(socrata_dataset_identifier)
    movie_locations = []
    marker = 0

    for movie in dataset:
        if movie['title'] == title:
            if 'locations' in movie:
                lat, lng = get_coordinates(movie['locations'])

                if lat != 0 and lng != 0:
                    marker += 1
                    movie_locations.append({
                        'title': movie['locations'],
                        'lat': lat,
                        'lng': lng,
                        'marker': 'marker' + str(marker)
                    })

    return templates.TemplateResponse('home.html', {
        'request': request,
        'API_KEY': GOOGLE_API_KEY,
        'movie_locations': movie_locations,
        'titles': titles
    })
