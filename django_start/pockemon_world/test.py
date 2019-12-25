from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse
import requests
from pockemon_world.views import POKEMON_API
from unittest import mock

class MockResponse:
    def json(self):
        return {"test": "invalid value"}

class StatusCheck(TestCase):
    client = Client()

    def test_helthcheck(self):
        response = self.client.get(reverse('healthcheck'))
        assert response.status_code == HTTPStatus.OK

    def test_index_page_status(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == HTTPStatus.OK

    def test_warehouse_page_status(self):
        response = self.client.get(reverse('warehouse'))
        assert response.status_code == HTTPStatus.OK

class PageContentCheck(TestCase):
    client = Client()

    def test_pokemon_api_valid_content(self):
        response = requests.get(POKEMON_API + 'type/3').json()
        pokemons = response['pokemon']
        self.assertIn('pokemon', response)
        for p in pokemons:
            with self.subTest(p=p):
                self.assertIn('pokemon', p)
                self.assertIn('name', p['pokemon'])

    @mock.patch('requests.get', return_value=MockResponse())
    def test_pokemon_api_invalid_content(self, value):
        response = requests.get(POKEMON_API + 'type/3')
        resp = response.json()
        with self.assertRaises(KeyError):
            self.client.get(reverse('warehouse'))
