from http.client import responses

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from planets.models import Planet

@pytest.mark.django_db
class TestPlanetApi:
    def setup_method(self):
        self.client = APIClient()
        self.list_url = reverse("planet-list")

    def test_create_planets(self):
        data = {"name": "Tatooine", "climates": "arid", "population": "200000"}
        response = self.client.post(self.list_url, data, format='json')

        response_data = response.data
        print(f'Response Data : {response_data}')
        assert response.status_code == 200 or 201
        assert response_data.get('name') == "Tatooine"
        assert Planet.objects.count() == 1

    def test_list_planets(self):
        data = {"name": "Hoth", "climates": "frozen", "population": "600000"}
        self.client.post(self.list_url, data, format='json')
        data = {"name": "Endor", "climates": "temperate", "population": "8200000"}
        self.client.post(self.list_url, data, format='json')

        response = self.client.get(self.list_url)

        assert response.status_code == 200
        assert len(response.data) == 2
        assert {planet.get('name') for planet in response.data} == {"Hoth", "Endor"}

    def test_retrieve_planet(self):
        data = {"name": "Dagobah", "climate": "murky", "population": "600000"}
        planet = self.client.post(self.list_url, data, format='json')
        planet_id = planet.data.get('id')
        print(f'Id : {planet_id}')

        detail_url = reverse("planet-detail", args=[planet_id])
        response = self.client.get(detail_url)
        response_data = response.data

        assert response.status_code == 200
        assert response_data.get('name') == "Dagobah"

    def test_update_planet(self):
        planet = Planet.objects.create(name="Naboo", climates="temperate", population="4500000000")
        planet_id = planet.id
        detail_url = reverse("planet-detail", args=[planet_id])

        response = self.client.patch(detail_url, {"population": "4600000000"}, format="json")

        assert response.status_code == 200
        planet.refresh_from_db()
        assert planet.population == "4600000000"

    def test_delete_planet(self):
        planet = Planet.objects.create(name="Mustafar", climates="hot", population="20000")
        planet_id = planet.id
        detail_url = reverse("planet-detail", args=[planet_id])

        response = self.client.delete(detail_url)

        assert response.status_code == 204 or 200
        assert Planet.objects.count() == 0

