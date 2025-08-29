import requests
from .models import Planet

def fetch_and_store():
    endpoint = "https://swapi-graphql.netlify.app/.netlify/functions/index"
    query = """
    query {
      allPlanets {
        planets {
          name
          population
          terrains
          climates
        }
      }
    }
    """
    response = requests.post(endpoint, json={'query': query})
    data = response.json()
    print(f"Response Data : {data}")
    planets_list = data['data']['allPlanets']['planets']
    for item in planets_list:
        Planet.objects.create(
            name=item.get('name'),
            population=item.get('population') or 'unknown',
            climates=", ".join(item.get('climates')),
            terrains=", ".join(item.get('terrains'))
        )
