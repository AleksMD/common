import requests
from django.http import HttpResponse
import json

POKEMON_API = 'https://pokeapi.co/api/v2/' 

INDEX_PAGE = """
    <html>
        <head>
            <title>Pokemon</title>
        </head>
        <body>
            <a href="/warehouse">GIVE ME POKEMONS</a>
        </body>
    </html>
"""

def healthcheck(request):
    return HttpResponse('Ok')


def index(request):
    return HttpResponse(INDEX_PAGE)

def pockemon_warehouse(request):
    pokemons = requests.get(POKEMON_API + 'type/3').json()['pokemon']
    raw_response = [f"<li>{item['pokemon']['name']}</li>" for item in pokemons]
    pokemon_html_list = "<a href='/'>Back to the homepage</a>\n<ol>\n"
    for p in raw_response:
        pokemon_html_list += p
    response = pokemon_html_list + "\n</ol>"
    return HttpResponse(response)

